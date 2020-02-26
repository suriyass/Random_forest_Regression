import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Authenticator;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.PasswordAuthentication;
import java.net.URL;

public class sam {
	
	public void rescue(String r, String r1, String h) throws IOException
	{
		
			String res = null, res1 = null,res2 =  null,res3 =  null,res4 = null ;
	      String url = "https://bawd1.fyre.ibm.com:9443/ibm/iis/ds/api/engines/bawd1.fyre.ibm.com/monitors/os_cpu_usage_system/";
          url += r+"-"+r1;
          URL url1 = new URL(url);
          System.out.println(url1);	
          String url2 = "https://bawd1.fyre.ibm.com:9443/ibm/iis/ds/api/engines/bawd1.fyre.ibm.com/monitors/os_cpu_usage_total/";
          url2 += r+"-"+r1;
          URL url3 = new URL(url2);
          System.out.println(url3);	
          String url4 = "https://bawd1.fyre.ibm.com:9443/ibm/iis/ds/api/engines/bawd1.fyre.ibm.com/monitors/os_memory_physical_free/";
          url4 += r+"-"+r1;
          URL url5 = new URL(url4);
          System.out.println(url5);	
          String url6 = "https://bawd1.fyre.ibm.com:9443/ibm/iis/ds/api/engines/bawd1.fyre.ibm.com/monitors/os_memory_virtual_free/";
          url6 += r+"-"+r1;
          URL url7 = new URL(url6);
          System.out.println(url7);	
          String url8 = "https://bawd1.fyre.ibm.com:9443/ibm/iis/ds/api/engines/bawd1.fyre.ibm.com/monitors/os_filesystem_free/";
          url8 += r+"-"+r1;
          URL url9 = new URL(url8);
          System.out.println(url9);	
		String readLine=null;
		HttpURLConnection conection = (HttpURLConnection) url1.openConnection();
		HttpURLConnection conection1 = (HttpURLConnection) url3.openConnection();
		HttpURLConnection conection2 = (HttpURLConnection) url5.openConnection();
		HttpURLConnection conection3 = (HttpURLConnection) url7.openConnection();
		HttpURLConnection conection4 = (HttpURLConnection) url9.openConnection();
        Authenticator.setDefault(new Authenticator()
        {
        	@Override
	    protected PasswordAuthentication getPasswordAuthentication()
        	{          
	       String login = "isadmin";
	       String password = "ibm_0123";
	       return new PasswordAuthentication(login, password.toCharArray());
        	}
        });
conection.setRequestMethod("GET");
conection.setRequestProperty("Accept", "application/json");
conection1.setRequestMethod("GET");
conection1.setRequestProperty("Accept", "application/json");
conection2.setRequestMethod("GET");
conection2.setRequestProperty("Accept", "application/json");
conection3.setRequestMethod("GET");
conection3.setRequestProperty("Accept", "application/json");
conection4.setRequestMethod("GET");
conection4.setRequestProperty("Accept", "application/json");
int responseCode = conection.getResponseCode();
int responseCode1 = conection1.getResponseCode();
int responseCode2 = conection2.getResponseCode();
int responseCode3 = conection3.getResponseCode();
int responseCode4 = conection4.getResponseCode();

System.out.println("response code:"+ responseCode);
System.out.println("response code:"+ responseCode1);
System.out.println("response code:"+ responseCode2);
System.out.println("response code:"+ responseCode3);
System.out.println("response code:"+ responseCode4);
if ((responseCode == HttpURLConnection.HTTP_OK) && (responseCode1 == HttpURLConnection.HTTP_OK)&&(responseCode2 == HttpURLConnection.HTTP_OK)&&(responseCode3 == HttpURLConnection.HTTP_OK)&&(responseCode4 == HttpURLConnection.HTTP_OK))
{
	BufferedReader in = new BufferedReader(
        new InputStreamReader(conection.getInputStream()));
	BufferedReader in1 = new BufferedReader(
	        new InputStreamReader(conection1.getInputStream()));
	BufferedReader in2 = new BufferedReader(
	        new InputStreamReader(conection2.getInputStream()));
	BufferedReader in3 = new BufferedReader(
	        new InputStreamReader(conection3.getInputStream()));
	BufferedReader in4 = new BufferedReader(
	        new InputStreamReader(conection4.getInputStream()));
    StringBuffer response = new StringBuffer();
    StringBuffer response1 = new StringBuffer();
    StringBuffer response2 = new StringBuffer();
    StringBuffer response3 = new StringBuffer();
    StringBuffer response4 = new StringBuffer();
    while ((readLine = in .readLine()) != null) 
    {
        response.append(readLine);
    } in .close();
    while ((readLine = in1 .readLine()) != null) 
    {
        response1.append(readLine);
    } in1 .close();
    while ((readLine = in2 .readLine()) != null) 
    {
        response2.append(readLine);
    } in1 .close();
    while ((readLine = in3 .readLine()) != null) 
    {
        response3.append(readLine);
    } in1 .close();
    while ((readLine = in4 .readLine()) != null) 
    {
        response4.append(readLine);
    } in1 .close();
    int x = response.lastIndexOf("timeWeightedAvg");
    int y = response.indexOf("type");
    int x1 = response1.lastIndexOf("timeWeightedAvg");
    int y1 = response1.indexOf("type");
    int x2 = response2.lastIndexOf("timeWeightedAvg");
    int y2 = response2.indexOf("type");
    int x3 = response3.lastIndexOf("timeWeightedAvg");
    int y3 = response3.indexOf("type");
     res= response.substring(x+17, y-5);
     System.out.println(res);
     res1= response1.substring(x1+17, y1-5);
     System.out.println(res1);
     res2= response2.substring(x2+17, y2-5);
     System.out.println(res2);
     res3= response3.substring(x3+17, y3-5);
     System.out.println(res3);
     res4= response4.substring(278, 285);
     System.out.println(res4);
    } 
else 
{
    System.out.println("GET NOT WORKED");
}
StringBuilder sb = new StringBuilder();

FileWriter fileWriter = new FileWriter("Book3.csv", true); //Set true for append mode
PrintWriter writer = new PrintWriter(fileWriter);
			  sb.append(res);
    		sb.append(',');
    		sb.append(res1);
    		sb.append(',');
    		sb.append(res2);
    		sb.append(',');
    		sb.append(res3);
    		sb.append(',');
    		sb.append(res4);
    		sb.append(',');
    		sb.append(h);
    		sb.append('\n');

    		
    		writer.write(sb.toString());
    		System.out.println("Done");
            writer.flush();
            writer.close();


	}

}
