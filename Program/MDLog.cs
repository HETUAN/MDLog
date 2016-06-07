using System;
using System.IO;
using System.Text;
using System.Collections.Generic;

class Test
{
    const string mdDir = @"md";
    const string jsonPath = @"Data/files.json";
    static void Main()
    {
        Console.WriteLine("Hello world");
        string jsonStr = GetMdListJson();
        WriteJson(jsonStr);
        Console.WriteLine(jsonStr);
        Console.ReadKey();
    }
    
    public static string GetMdListJson() {
        string[] files = Directory.GetFiles(mdDir);
        if(files.Length<=0)
            return "";
        StringBuilder jsonsb = new StringBuilder();
        jsonsb.AppendLine("{\"files\":[");
        for (int i = 0; i < files.Length; i++)
        {
            jsonsb.AppendLine(ReadHead(files[i]));
        }
        jsonsb = jsonsb.Remove(jsonsb.Length - 3, 1); 
        jsonsb.AppendLine("]}");
        return jsonsb.ToString();
    }
    
    public static string ReadHead(string path){
        StreamReader sr = new StreamReader(path);
        string line = string.Empty;
        StringBuilder headJson = new StringBuilder();
        while ((line = sr.ReadLine()) != null)
        {
            line = line.Trim();
            if (line == "------")
                break;
            headJson.AppendLine(line);
        }
        int idx = headJson.ToString().LastIndexOf("}");
        if (idx > 0)
        {
            headJson = headJson.Insert(idx - 2, ",\n\"url\":\"" + path.Replace("\\","/") + "\"");
        }
            headJson.Append(",");
        return headJson.ToString();
    }

    public static void WriteJson(string data){
        try
        {
            if(!File.Exists(jsonPath)){
                Console.WriteLine("2");
                using(FileStream fs = File.Create(Path.Combine(Environment.CurrentDirectory , jsonPath))){
                }
            }
            using (StreamWriter sw = new StreamWriter(jsonPath))
            { 
                sw.Write(data);
                Console.WriteLine("SUCCESS"); 
            }
        }
        catch (System.Exception ex)
        {
            Console.WriteLine(ex.Message+"  -- 请确定文件目录存在！");
        }
    }
 
}
 