Title: Phonegap 初始化大数据到 Sqlite
Date: 2013-10-21 21:00
Category: phonegap
Tags: phonegap, SQLitePlugin
Authors: liuwei

客户需要做离线App, 也就是说现在需要将Sqlserver数据库中现有的数据全部初始化至App本地数据库。如果一条条insert，一共有接近70万条数据。显然使用Web sql 5M的容量限制无法满足要求。
于是采用PhoneGap SQLitePlugin,地址: https://github.com/lite4cordova/Cordova-SQLitePlugin

为项目添加好插件之后，运行，带来另一个问题，执行insert语句依旧很慢。之后，便采用5000条语句使用一个事务的方式批量插入，对10万条数据进行了测试，如下：

	executeSqlBatch icount:0 insertSumCount:20 Time:3:00:29 PM GMT+08:00
	
	executeSqlBatch icount:1 insertSumCount:20 Time:3:00:32 PM GMT+08:00
	
	executeSqlBatch icount:2 insertSumCount:20 Time:3:00:39 PM GMT+08:00
	
	executeSqlBatch icount:3 insertSumCount:20 Time:3:00:48 PM GMT+08:00
	
	executeSqlBatch icount:4 insertSumCount:20 Time:3:01:01 PM GMT+08:00
	
	executeSqlBatch icount:5 insertSumCount:20 Time:3:01:16 PM GMT+08:00
	
	executeSqlBatch icount:6 insertSumCount:20 Time:3:01:35 PM GMT+08:00
	
	executeSqlBatch icount:7 insertSumCount:20 Time:3:01:58 PM GMT+08:00
	
	executeSqlBatch icount:8 insertSumCount:20 Time:3:02:26 PM GMT+08:00
	
	executeSqlBatch icount:9 insertSumCount:20 Time:3:02:56 PM GMT+08:00
	
	executeSqlBatch icount:10 insertSumCount:20 Time:3:03:29 PM GMT+08:00
	
	executeSqlBatch icount:11 insertSumCount:20 Time:3:04:06 PM GMT+08:00
	
	executeSqlBatch icount:12 insertSumCount:20 Time:3:04:47 PM GMT+08:00
	
	executeSqlBatch icount:13 insertSumCount:20 Time:3:05:31 PM GMT+08:00
	
	executeSqlBatch icount:14 insertSumCount:20 Time:3:06:19 PM GMT+08:00
	
	executeSqlBatch icount:15 insertSumCount:20 Time:3:07:08 PM GMT+08:00
	
	executeSqlBatch icount:16 insertSumCount:20 Time:3:08:01 PM GMT+08:00
	
	executeSqlBatch icount:17 insertSumCount:20 Time:3:08:58 PM GMT+08:00
	
	executeSqlBatch icount:18 insertSumCount:20 Time:3:11:13 PM GMT+08:00
	
	executeSqlBatch icount:19 insertSumCount:20 Time:3:12:17 PM GMT+08:00
	
	executeSqlBatch icount:20 insertSumCount:20 Time:3:13:23 PM GMT+08:00
	
可以看到，10万条insert语句，采用每5000条语句提交一次事务的方式，一共花了12分54秒。而且每次执行时间比前一次时间要长，并且随着数据量越大，以后每次的执行时间将更长，因为sqlite采用的是文本形式的数据库，每次对数据库的操作都会进行I/O操作。显然，如此漫长的等待时间，客户是难以接受的。

最后解决的办法是，将Sqlserver中现有的数据导出成sqlite数据库文件，如xxx.db,之后将该文件放在程序中，待App第一次启动的时候，将该xxx.db数据库文件拷贝到相应的目录，如android默认是在/data/data/packagename/database目录下，iphone默认是在/Applications/APP串/Documents目录下。
所以，具体的解决办法如下：

Phonegap IOS版:

1,将需要导入的数据库文件拷贝到Resources目录下.

2, AppDelegate.m文件中添加如下代码:

	- (void)createEditableCopyOfDatabaseIfNeeded {
	// First, test for existence. BOOL success=NO;
	BOOL success=NO;
	NSString *dbFileName = @"import.db";
	NSFileManager *fileManager = [NSFileManager defaultManager];
	NSError *error; NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
	NSString *documentsDirectory = [paths objectAtIndex:0]; NSString *writableDBPath = [documentsDirectory stringByAppendingPathComponent:dbFileName];
	success = [fileManager fileExistsAtPath:writableDBPath];
	if (success){ NSLog(@"数据库存在");
	return;}
	// The writable database does not exist, so copy the default to the appropriate location.
	NSString *defaultDBPath = [[[NSBundle mainBundle] resourcePath] stringByAppendingPathComponent:dbFileName];
	success = [fileManager copyItemAtPath:defaultDBPath toPath:writableDBPath error:&error];
	if (!success) {
	NSAssert1(0, @"Failed to create writable database file with message '%@'.", [error localizedDescription]);
	}else {
	NSLog(@"createEditableCopyOfDatabaseIfNeeded initialize success");
	} }

在didFinishLaunchingWithOptions中调用：

	[self createEditableCopyOfDatabaseIfNeeded];

3, 在PhoneGap SQLitePlugin中打开数据库的代码为：

	db = window.sqlitePlugin.openDatabase({name: "import.db"});
	
Phonegap Android版：

1,将需要导入的数据库文件拷贝到res/raw目录下.

2,添加DataBaseUtil.java文件

	import java.io.File; 
	import java.io.FileOutputStream; 
	import java.io.IOException; 
	import java.io.InputStream; 
	
	import android.content.Context; 
	import android.database.sqlite.SQLiteDatabase; 
	import android.database.sqlite.SQLiteException; 
	
	public class DataBaseUtil { 
	
	    private Context context; 
	    public static String dbName = "texonline.db";// 数据库的名字 
	    private static String DATABASE_PATH;// 数据库在手机里的路径 
	
	    public DataBaseUtil(Context context) { 
	        this.context = context; 
	        String packageName = context.getPackageName(); 
	        DATABASE_PATH="/data/data/"+packageName+"/databases/"; 
	    } 
	
	    /** 
	     * 判断数据库是否存在 
	     *  
	     * @return false or true 
	     */ 
	    public boolean checkDataBase() { 
	        SQLiteDatabase db = null; 
	        try { 
	            String databaseFilename = DATABASE_PATH + dbName; 
	            System.out.println("checkDataBase=>"+databaseFilename); 
	            db = SQLiteDatabase.openDatabase(databaseFilename, null,SQLiteDatabase.OPEN_READONLY); 
	        } catch (SQLiteException e) { 
	
	        } 
	        if (db != null) { 
	            db.close(); 
	        } 
	        return db != null ? true : false; 
	    } 
	
	    /** 
	     * 复制数据库到手机指定文件夹下 
	     *  
	     * @throws IOException 
	     */ 
	    public void copyDataBase() throws IOException { 
	        String databaseFilenames = DATABASE_PATH + dbName; 
	        File dir = new File(DATABASE_PATH); 
	        if (!dir.exists())// 判断文件夹是否存在，不存在就新建一个 
	            dir.mkdir(); 
	        FileOutputStream os = new FileOutputStream(databaseFilenames);// 得到数据库文件的写入流 
	        InputStream is = context.getResources().openRawResource(R.raw.texonline);// 得到数据库文件的数据流 
	        byte[] buffer = new byte[8192]; 
	        int count = 0; 
	        while ((count = is.read(buffer)) > 0) { 
	            os.write(buffer, 0, count); 
	            os.flush(); 
	        } 
	        is.close(); 
	        os.close(); 
	        System.out.println("copyDataBase success"); 
	    } 
	}
3,在继承自DroidGap的activity里添加如下方法，并在onCreate里调用。

	@Override 
	    public void onCreate(Bundle savedInstanceState) 
	    { 
	        super.onCreate(savedInstanceState); 
	        // Set by <content src="index.html" /> in config.xml 
	        super.setIntegerProperty("loadUrlTimeoutValue", 60000); 
	        super.loadUrl(Config.getStartUrl(),10000); 
	        copyDataBaseToPhone(); 
	    } 
	
	    private void copyDataBaseToPhone() { 
	        DataBaseUtil util = new DataBaseUtil(this); 
	        // 判断数据库是否存在 
	        boolean dbExist = util.checkDataBase(); 
	
	        if (dbExist) { 
	            Log.i("tag", "The database is exist."); 
	        } else {// 不存在就把raw里的数据库写入手机 
	            try { 
	                util.copyDataBase(); 
	            } catch (IOException e) { 
	                throw new Error("Error copying database"); 
	            } 
	        } 
	    }
	    
4,在PhoneGap SQLitePlugin中打开数据库的代码为

	db = window.sqlitePlugin.openDatabase({name: "import.db"});
	
