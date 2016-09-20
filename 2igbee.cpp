#include"STC12C5A08S2.h"
#include"串口.h"
#include"DS1302.h"
#include"LCD12864.h"
#include"zigbee.h"
//#include"key.h"
#include <stdio.h>

#define uint unsigned int
#define uchar unsigned char

sbit  WaterIO=P2^0;

uint CycleTime;	 //循环周期，数据上传周期，这里定时10分钟 
uchar LastTime;		 //上次的分钟数
uint Timing;
uint WaterTime;		//浇灌时间

uchar  xdata SS[]="0123456789ABCDE";
uchar  flag;
uchar  flag1;	
uchar  receive_count;
uchar  receive_dat[14];
uchar  receive_count1;
uchar  receive_dat1[12];
uchar  SendDat[]=

{0xEE,0XB1,0X10,0X00,0X0A,0X00,0X0A,0X00,0X00,0X2E,0X00,0XFF,0XFC,0XFF

,0xff};



main()
{

	 bit PleseDateFlag,ControlFlag=0;
	 uchar i,num=0;
	 int ConvertTemp1,ConvertTemp2,ConvertHumi1;
     CycleTime=30;
	 Timing=30;
	 flag=0;
	 flag1=0;
	 receive_count=0;
	 receive_count1=0;
    UART1_Init(0XD9,0,1);//9600 1T模式 不倍频
	UART2_Init(0XD9,0,1);//9600 1T模式 不倍频UART1_Init

(0XD9,0,1);//9600 1T模式 不倍频
//	Init_ST7920();		  //液晶初始化
	Ds1302_Init();        //ds1302初始化
	
	 // Establish_Rout();
	 while(1)
	 {
	   	 Ds1302_Read_Time();
		 //判断是否到达请求数据的时间
	   	 if(LastTime!=time_buf[5])
		 {
		 	LastTime=time_buf[5];
			Timing++;
			if(Timing>=CycleTime)
			{
			  PleseDateFlag=1;
			  Timing=0;
			}
			

			if(WaterTime>0)
			 {
			     
			 	 WaterTime--;
			
			 }
			 else 
			   {
			     
				 WaterTime=0;
				 
			   }
				 long_DAT[6]=WaterTime;
			     long_rout[4]=0x04;
			     long_DAT[4]=0x04;
			     Establish_Rout();
		 	     SendDate();
				 flag=0;
	             receive_count=0;
		 }
		 //如果时间到，则发送数据
		 if(PleseDateFlag)
		 {	 
		     long_rout[4]=0x02;
			 long_DAT[4]=0x02;
			 Establish_Rout();
		 	 SendDate();
			 PleseDateFlag=0;

		 }	
		  
		 if(flag)
		 {
		    DelayMs(50);
		    if(receive_dat[0]==0x00)
		     {
		 	    
			    ConvertTemp1=receive_dat[3]

*256+receive_dat[4];
			    
			    ConvertHumi1=receive_dat[5]

*256+receive_dat[6];
			    


			    flag=0;
	            receive_count=0;

				long_rout[4]=0x03;
			    long_DAT[4]=0x03;
			    Establish_Rout();
		 	    SendDate();
				flag=0;
	            receive_count=0;

	         
		   }
		   else if(receive_dat[0]==0x01)
		   {
			    
				ConvertTemp2=((receive_dat[3]

*256+receive_dat[4])+ConvertTemp1)*2;
				long_GPRSDAT[0]=0x00;
				long_GPRSDAT[1]=0x00;
				long_GPRSDAT[2]=0x00;
				long_GPRSDAT[3]=ConvertTemp2/1000;
			    long_GPRSDAT[4]=(ConvertTemp2%1000)/100;
			    long_GPRSDAT[5]=(ConvertTemp2%100)/10;
				long_GPRSDAT[6]=ConvertHumi1/1000;
			    long_GPRSDAT[7]=(ConvertHumi1%1000)/100;
			    long_GPRSDAT[8]=(ConvertHumi1%100)/10; 
				SendDat[6]=0x0A;
				SendDat[7]=long_GPRSDAT[6]+0x30;
				SendDat[8]=long_GPRSDAT[7]+0x30;
				SendDat[10]=long_GPRSDAT[8]+0x30;
				for(i=0;i<sizeof(SendDat);i++)
                  {
	                 UART2_SendOneChar(SendDat[i]);
			      }
				SendDat[6]=0x0B;
				SendDat[7]=long_GPRSDAT[3]+0x30;
				SendDat[8]=long_GPRSDAT[4]+0x30;
				SendDat[10]=long_GPRSDAT[5]+0x30;
				for(i=0;i<sizeof(SendDat);i++)
                  {
	                 UART2_SendOneChar(SendDat[i]);
			      }
			    
		
			    for(i=0;i<sizeof(long_GPRSDAT);i++)
                  {
	                 UART1_SendOneChar(SS[long_GPRSDAT[i]]);
			      }
			     DelayMs(100);
				 flag=0;
	             receive_count=0;
		   }
		 
		 }
	
		 if(flag1)
		   {
		      DelayMs(50);
			  if(receive_dat1[0]==0x00)
			    { 
				 if(!ControlFlag)
				 {
				  WaterTime=receive_dat1[1] ;
				  	long_rout[4]=0x04;
			         long_DAT[4]=0x04;
					 long_DAT[6]=WaterTime;
			         Establish_Rout();
		 	         SendDate();
				  }
			   	 }
				else if((receive_dat1[0]==0xEE)&&

(receive_dat1[4]==0x0B)&&(receive_dat1[6]==0x19))
			    { 
				     if(receive_dat1[9]==0x00)
					  {
					   WaterTime=50;
					   ControlFlag=1;
					   
					   }
					  else if(receive_dat1[9]

==0x01)
					  {
					   WaterTime=0;
					   ControlFlag=0;
					   }
					 
					 
				     long_rout[4]=0x04;
			         long_DAT[4]=0x04;
					 long_DAT[6]=WaterTime;
			         Establish_Rout();
		 	         SendDate();
			   	 } 
			  	     
				  
				  flag1=0;
	              receive_count1=0;
		   }
		  
	  }
	  
}

void UART1_Int(void) interrupt 4 
{   

    if (RI == 1)   
    {  
          RI = 0 ; 
		  receive_dat1[receive_count1]=SBUF;
		  receive_count1++;
		  flag1=1;
		  
    }   
} 

 void UART2_Int(void) interrupt 8   
{   

 
    if ((S2CON & 0x01) == 1)   
    { 
	    
        S2CON &= 0xFE;  
		
		receive_dat[receive_count]=S2BUF;
		receive_count++;
		
		  	flag=1;
		
    }      

} 


#include"STC12C5A08S2.h"

#define uint unsigned int
#define uchar unsigned char

uchar  flag;
uchar  flag1;
uchar  receive_count;
uchar  receive_dat[14];
uchar  receive_count1;
uchar  receive_dat1[12];

uchar  long_rout[]={0XA5,0X03,0XD3,0X00,0X02,0X5A};	               

    
uchar  long_DAT[]={0XA5,0X07,0XD1,0X00,0X02,0X00,0X00,0X00,0X00,0X5A};
uchar  long_GPRSDAT[]={0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};

/*----------------------------------------
内容：建立路由连接。首先发送路由表，延时50MS
      检测是否有数据返回，查询30次，如果是
	  无数据则说明zigbee出现问题，则再次发送
	  路由表，进行重新检测；如果返回数据，且
	  为A5 01 A3 5A ,则查找路由表超时，重新发
	  送；如果为A5 07 D3 00 00 AF 00 02 00 5A 
	  则发送成功，且返回第5位
----------------------------------------*/
void Establish_Rout(void)
{
    uchar i,m=1;
	uint j=0 ;
	flag=0;
	receive_count=0;
  
	
	for(i=0;i<sizeof(long_rout);i++)
      {
	     UART2_SendOneChar(long_rout[i]);
	  }
	  DelayMs(500);
	  while(flag==0)
	  {
	  	 DelayMs(200);
		 j++;
		 if(j>=20)
		 {
			for(i=0;i<sizeof(long_rout);i++)
              {
	            UART2_SendOneChar(long_rout[i]);
	          }
			   j=0;
		 }
	  }
	  
	  if(receive_dat[0]==0xA5)
		 {
		  if(receive_count>8)
	        {
			 
			  long_GPRSDAT[1]=receive_dat[5];
			 }
		   
		     flag=0;
			 receive_count=0;
		 } 	
		 
	
             flag=0;
			 receive_count=0;
}
/*----------------------------------------
内容：把采集到的数据通过zigbee发送到中间节点
      上来，如果返回的数据为A5 01 00 5A，则
	  发送正确，如果为A5 01 A4 5A，则重新建
	  立路由连接，并重新发送
----------------------------------------*/
void SendDate()
{
	 uchar i,m=1;
	 
	 flag=0;
	 receive_count=0;
	 for(i=0;i<sizeof(long_DAT);i++)
        {
	      UART2_SendOneChar(long_DAT[i]);
	    }
		while(flag==0); //等待数据返回
		
	  while(m)
	  {
	   	   DelayMs(200);
	  	if(receive_dat[2]==0x00)
		 {
		 	m=0;
			flag=0;	        
	        receive_count=0;
	        

		 }
		 else 
		 {
		 	Establish_Rout();
			flag=0;
	        
	        receive_count=0;
	        
			for(i=0;i<sizeof(long_DAT);i++)
              {
	             UART2_SendOneChar(long_DAT[i]);
	          }
		    while(flag==0); //等待数据返回
		 }
		 
	  }
}


/*********************************************************************

***************/


#include"STC12C5A08S2.h"

#define uint unsigned int
#define uchar unsigned char

#define OpenUART1()		ES=1
#define	CloseUART1()	ES=0
#define	OpenUART2()		IE2|=0x01
#define	CloseUART2()	IE2&=0xFE



void UART1_Init(uchar RELOAD, bit doubleBaud, bit timeMod)   
{   
    SCON |= 0x50;       //串口1方式1,接收充许   
  
    BRT = RELOAD;       //波特率2400   
  
    if (timeMod == 1)       //1T   
    {   
        //T0x12   T1x12   UM0x6   BRTR    S2SMOD  BRTx12  EXTRAM  

S1BRS   
        AUXR |= 0x15;       //串口1使用独立波特率发生器，独立波特率发

生器1T   
    }   
    else                    //12T   
    {   
        AUXR |= 0x11;   
    }   
  
    if (doubleBaud == 1)   
    {   
        PCON |= 0x80;     //波特率加倍   
    }   
    else  
    {   
        PCON &= 0x7F;     //波特率不加倍   
    }   
  
    EA = 1;   
    ES = 1;             //充许串口1中断   
}  
/*  
 * 函 数 名：UART1_SendOneChar  
 * 功能描述：串口1发送一个字符  
 * 输入参数：val:要发送的字符  
 * 返 回 值：无  
 */  
void UART1_SendOneChar(uchar val)   
{   
    //ES = 0;                   //关闭串口1中断   
    OpenUART1();
 	CloseUART2();
    SBUF = val;   
    while(TI == 0);   
    TI = 0;   
  	OpenUART2();
    //ES = 1;                  //恢复串口1中断   
}  






/*********************************************************************

****
Function:	定时器初始化
			BRT定时器用作串口2波特率发生器,9600bps
No Return
**********************************************************************

***/
void Timer_Init(void)
{
	BRT  = 0xFD;//reload count
}

/*********************************************************************

****
Function:	串口初始化
			串口2:9600bps,8bit,NONE,1 stop
No Return
**********************************************************************

***/
void Uart_Init(void)
{
//	S2CON = 0x50;	//8bit mod 1
//	AUXR = 0x10;	//BRT start
	AUXR1 = 0x00;	//将串口2从P1口移到P4口
}

/*  
 * 函 数 名：UART2_Init  
 * 功能描述：串口2初始化  
 * 输入参数：RELOAD:BRT初值；  
 *           doubleBaud:0波特率不加倍，1波特率加倍  
 *           timeMod:0独立波特率发生器12T模式，1为1T模式  
 * 返 回 值：无  
 */  
void UART2_Init(uchar RELOAD, bit doubleBaud, bit timeMod)   
{   
    //S2SM0  S2SM1   S2SM2   S2REN   S2TB8   S2RB8   S2TI     S2RI   
    S2CON |= 0x50;      //串口2,方式1，接收充许   
 // Uart_Init();
    BRT = RELOAD;   
  
    if (timeMod == 1)       //1T   
    {   
        //T0x12   T1x12   UM0x6   BRTR    S2SMOD  BRTx12  EXTRAM  

S1BRS   
        AUXR |= 0x14;       //串口1使用独立波特率发生器，独立波特率发

生器1T   
    }   
    else                    //12T   
    {   
        AUXR = (AUXR | 0x10) & 0xFB;   
    }   
  
    if (doubleBaud == 1)   
    {   
        AUXR |= 0x08;       //波特率加倍   
    }   
    else  
    {   
        AUXR &= 0xF7;       //波特率不加倍   
    }   
  
    EA = 1;    
    //-       -       -       -       -       -       ESPI    ES2   
    IE2 |= 0x01;            //充许串口2中断              
} 

/*  
 * 函 数 名：UART2_SendOneChar  
 * 功能描述：串口2发送一个字符  
 * 输入参数：val:要发送的字符  
 * 返 回 值：无  
 */  
void UART2_SendOneChar(uchar val)   
{   
    //IE2 = 0x00;                 //关闭串口2中断   
    OpenUART2();
  	CloseUART1();
    S2BUF = val;       
    while ((S2CON & 0x02) == 0);   
    S2CON &= 0xFD;   
  	  OpenUART1();
    //IE2 = 0x01;                //恢复串口2中断   
} 


#include"STC12C5A08S2.h"
#define uint unsigned int
#define uchar unsigned char

sbit SCK=P1^4;		
sbit SDA=P1^5;		
sbit RST0=P1^6;



unsigned char time_buf[8] ;                         //空年月日时分秒周
//复位脚
#define RST_CLR	RST0=0//电平置低
#define RST_SET	RST0=1//电平置高


//双向数据
#define IO_CLR	SDA=0//电平置低
#define IO_SET	SDA=1//电平置高
#define IO_R	SDA  //电平读取


//时钟信号
#define SCK_CLR	SCK=0//时钟信号
#define SCK_SET	SCK=1//电平置高


#define ds1302_sec_add			0x80		//秒数据地址
#define ds1302_min_add			0x82		//分数据地址
#define ds1302_hr_add			0x84		//时数据地址
#define ds1302_date_add			0x86		//日数据地址
#define ds1302_month_add		0x88		//月数据地址
#define ds1302_day_add			0x8a		//星期数据地址
#define ds1302_year_add			0x8c		//年数据地址
#define ds1302_control_add		0x8e		//控制数据地址
#define ds1302_charger_add		0x90 				

	 
#define ds1302_clkburst_add		0xbe




/*------------------------------------------------
           向DS1302写入一字节数据
------------------------------------------------*/
void Ds1302_Write_Byte(unsigned char addr, unsigned char d)
{

	unsigned char i;
	RST_SET;	
	
	//写入目标地址：addr
	addr = addr & 0xFE;     //最低位置零
	for (i = 0; i < 8; i ++) 
	    { 
		if (addr & 0x01) 
		    {
			IO_SET;
			}
		else 
		    {
			IO_CLR;
			}
		SCK_SET;
		SCK_CLR;
		addr = addr >> 1;
		}
	
	//写入数据：d
	for (i = 0; i < 8; i ++) 
	   {
		if (d & 0x01) 
		    {
			IO_SET;
			}
		else 
		    {
			IO_CLR;
			}
		SCK_SET;
		SCK_CLR;
		d = d >> 1;
		}
	RST_CLR;					//停止DS1302总

线
}

/*------------------------------------------------
           从DS1302读出一字节数据
------------------------------------------------*/

unsigned char Ds1302_Read_Byte(unsigned char addr) 
{

	unsigned char i;
	unsigned char temp;
	RST_SET;	

	//写入目标地址：addr
	addr = addr | 0x01;//最低位置高
	for (i = 0; i < 8; i ++) 
	    {
	     
		if (addr & 0x01) 
		   {
			IO_SET;
			}
		else 
		    {
			IO_CLR;
			}
		SCK_SET;
		SCK_CLR;
		addr = addr >> 1;
		}
	
	//输出数据：temp
	for (i = 0; i < 8; i ++) 
	    {
		temp = temp >> 1;
		if (IO_R) 
		   {
			temp |= 0x80;
			}
		else 
		   {
			temp &= 0x7F;
			}
		SCK_SET;
		SCK_CLR;
		}
	
	RST_CLR;	//停止DS1302总线
	return temp;
}

/*------------------------------------------------
           从DS1302读出时钟数据
------------------------------------------------*/
void Ds1302_Read_Time(void)  
{ 
   	 
	time_buf[1]=Ds1302_Read_Byte(ds1302_year_add);		//年 
	time_buf[2]=Ds1302_Read_Byte(ds1302_month_add);		//月 
	time_buf[3]=Ds1302_Read_Byte(ds1302_date_add);		//日 
	time_buf[4]=Ds1302_Read_Byte(ds1302_hr_add);		//时 
	time_buf[5]=Ds1302_Read_Byte(ds1302_min_add);		//分 
	time_buf[6]=(Ds1302_Read_Byte(ds1302_sec_add))&0x7F;//秒 
	time_buf[7]=Ds1302_Read_Byte(ds1302_day_add);		//周 


	
}

/*------------------------------------------------
                DS1302初始化
------------------------------------------------*/
void Ds1302_Init(void)
{
	
	RST_CLR;			//RST脚置低
	SCK_CLR;			//SCK脚置低
    Ds1302_Write_Byte(ds1302_sec_add,0x00);				

 
}
