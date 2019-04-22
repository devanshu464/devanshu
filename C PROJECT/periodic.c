#include<stdio.h>
#include<windows.h>
#include<string.h>
#include<stdlib.h>
struct element{
		char name[20];
		char sb[5];
		int atm;
		float atms;
		char block;
		char atc[20];
		char prop[250];
	       }p,q;
int rw,cl;
FILE*fp;
void add();
void explor();
void print();
void mainscreen();
//define gotoxy for ANSI C compilers.
void gotoxy(short x,short y)
{
	COORD pos={x,y};
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),pos);
	
}
void main()
{
	int a,i,n,y;
	char c,d;
	char date1[15],date2[15],string1[20];
	unsigned int tsz;

	system("cls");
	mainscreen();
	label1:

	gotoxy(22,15);
	system("COLOR 09");//used to color both screenbackground as well as font('0' set background color and '9' set font color)
	printf("Enter the corresponding no");gotoxy(22,19);
	printf("1.Add new Element Information");gotoxy(22,21);
	printf("2.Explore");gotoxy(22,23);
	printf("3.Quit");gotoxy(22,25);
	fflush(stdin);
	d=getch();
	switch(d)
	{
		case '1':
		      {
			add();
			break;
		      }
		case '2':
		      {
			explor();
			break;

			}
		case '3':
		      {
			system("cls");
			mainscreen();
			 gotoxy(30,24);
			printf("THANK U");gotoxy(30,26);
			printf("********BYE***********");
			getch();
			exit(1);
			break;
			}







		default:
		       {
			system("cls");
			mainscreen();
			gotoxy(22,11);
			printf("Wrong choice");gotoxy(22,13);
			 printf("Retype choice");
			goto label1;
			}

	}
	system("cls");
	mainscreen();
	goto label1;
}
void mainscreen()
{
	int i,j;
	system("cls");
	for(i=2,j=2;i<rw;j++)
	{
		if(j>15)
		j=2;

		gotoxy(i,2);
		printf("%c",'*');
		gotoxy(i,cl-1);
		printf("%c",'*');
		i++;

	}
	for(i=2,j=2;i<cl;i++,j++)
	{
		if(j>15)
		j=2;
		gotoxy(2,i);
		printf("%c",'*');
		gotoxy(rw-1,i);
		printf("%c",'*');

	}
	gotoxy(30,4);
	printf("Modern Periodic Table");
	gotoxy(37,6);
	printf("Digital");
	gotoxy(35,7);
	printf("-----------");
}
void add()
{
	char ch;
	label1:
	system("cls");
	mainscreen();
		gotoxy(15,14);
	printf("Enter the Information of Elements:");
	gotoxy(15,16);
	printf("Name:");

	gotoxy(15,18);
	printf("Symbol:");

	gotoxy(15,20);
	printf("Atomic No: ");

	gotoxy(15,22);
	printf("Atomic Wt: ");

	gotoxy(15,24);
	printf("Atomic Config:");

	gotoxy(15,26);
	printf("Block:");

	gotoxy(15,28);
	printf("Properties:");

	fflush(stdin);
	gotoxy(20,16);
	scanf("%[^\n]",p.name);
	p.name[0]=toupper(p.name[0]);

	fflush(stdin);
	gotoxy(23,18);
	scanf("%[^\n]",p.sb);
	p.sb[0]=toupper(p.sb[0]);

	fflush(stdin);
	gotoxy(25,20);
	scanf("%d",&p.atm);

	fflush(stdin);
	gotoxy(25,22);
	scanf("%f",&p.atms);

	fflush(stdin);
	gotoxy(29,24);
	scanf("%[^\n]",p.atc);

	fflush(stdin);
	gotoxy(21,26);
	scanf("%c",&p.block);
	p.block=toupper(p.block);
	if(p.block!='S'&&p.block!='P'&&p.block!='D'&&p.block!='F')
	p.block=' ';
	fflush(stdin);

	gotoxy(26,28);
	scanf("%[^\n]",p.prop);
	p.prop[0]=toupper(p.prop[0]);


	if((fp=fopen("data","ab+"))==NULL)
	{
		printf("Cannot open the file f1");
		getch();
		exit(1);
	}
	fwrite(&p,sizeof(p),1,fp);
	fclose(fp);
	printf("\n\n\n\t\tEnter 'y' for next record(y/n):");
	ch=getch();
	if(ch=='y')
	{
		goto label1;
	}

}
void explor()
{
	char d,c;
	FILE *f;
	int given_atmic_no,a,i,tsz,n;
	float given_atmic_mass;
	int flag;
	char string[20];
	startofexplore:
	system("cls");
	mainscreen();
	label6:
	gotoxy(22,15);
	printf("Enter the corresponding no");gotoxy(22,19);
	printf("1.Search by 'NAME'");gotoxy(22,21);
	printf("2.Search by SYMBOL");gotoxy(22,23);
	printf("3.Search by ATOMIC NUMBER");gotoxy(22,25);
	printf("4.Search by ATOMIC WEIGHT");gotoxy(22,27);
	printf("5.Elements of Diff. Blocks");gotoxy(22,29);
	printf("6.Return to main menu");
	gotoxy(25,32);
	fflush(stdin);
	d=getch();
	switch(d)
       {
		case '1':
		{
			system("cls");
			mainscreen();
			gotoxy(15,25);
			printf("Enter the Name of Element:");
			fflush(stdin);
			scanf("%[^\n]",string);
			printf("%s",string);
			string[0]=toupper(string[0]);
			if((fp=fopen("data","rb+"))==NULL)
			{
			system("cls");

			printf("\n cannot open the record file 1");
			getch();
			exit(1);
			}
			flag=1;
			while(fread(&p,sizeof(p),1,fp))
			{
				 if(strcmp(p.name,string)==0)
				{
					print();

					flag=0;

					break;
				 }

			}
			if(flag==1)
			{
				system("cls");
				mainscreen();
				gotoxy(25,25);
				printf("::No Element Available::");

			}

			fclose(fp);
			getch();
			break;
		}
		case '2':
		{
			system("cls");
			mainscreen();
			gotoxy(22,15);
			printf("Enter the symbol:");
			fflush(stdin);
			scanf("%[^\n]",string);
			printf("%s",string);
			string[0]=toupper(string[0]);
			if((fp=fopen("data","rb+"))==NULL)
			{
			system("cls");

			printf("\n cannot open the record file 1");
			getch();
			exit(1);
			}
			flag=1;
			while(fread(&p,sizeof(p),1,fp))
			{
				 if(strcmp(p.sb,string)==0)
				{
					print();
					flag=0;


					break;
				 }

			}
			if(flag==1)
			{
				system("cls");
				mainscreen();
				gotoxy(25,25);
				printf("::No Element Available::");

			}

			fclose(fp);
			getch();
			break;
		}
		case '6':
		{
			return;
		}
		case '3':
		{
			system("cls");
			mainscreen();
			gotoxy(15,25);
			printf("Enter the Atomic No. Element:");
			fflush(stdin);
			scanf("%d",&given_atmic_no);
			if((fp=fopen("data","rb+"))==NULL)
			{
			system("cls");

			printf("\n cannot open the record file 1");
			getch();
			exit(1);
			}
			flag=1;
			while(fread(&p,sizeof(p),1,fp))
			{
				 if(p.atm==given_atmic_no)
				{
					print();
					flag=0;

					break;
				 }

			}
			if(flag==1)
			{
				system("cls");
				mainscreen();
				gotoxy(25,25);
	//			textcolor(12);
				printf("::No Element Available::");

			}

			fclose(fp);
			getch();
			break;
		}
		case '4':
		{
			system("cls");
			mainscreen();
			gotoxy(15,22);
			printf("Enter the Atomic mass of Element:");
			fflush(stdin);
			scanf("%f",&given_atmic_mass);
			if((fp=fopen("data","rb+"))==NULL)
			{
			system("cls");

			printf("\n cannot open the record file 1");
			getch();
			exit(1);
			}
			flag=1;
			while(fread(&p,sizeof(p),1,fp))
			{
				 if(p.atms==given_atmic_mass)
				{
					print();
					flag=0;

					break;
				 }

			}
			if(flag==1)
			{
				system("cls");
				mainscreen();
				gotoxy(25,25);
				//textcolor(12);
				printf("::No Element Available::");

			}

			fclose(fp);
			getch();
			break;
		}
		case '5':
		{

			system("cls");
			mainscreen();
			gotoxy(15,25);
			printf("Enter the Block:");
			fflush(stdin);
			scanf("%c",&c);
			c=toupper(c);
			if((f=fopen("temp","wb+"))==NULL)
			{
			system("cls");

			printf("\n cannot open the temp file 1");
			getch();
			exit(1);
			}


			if((fp=fopen("data","rb+"))==NULL)
			{
			system("cls");

			printf("\n cannot open the record file 1");
			getch();
			exit(1);
			}
			flag=1;
			while(fread(&p,sizeof(p),1,fp))
			{
				 if(p.block==c)
				{
					fwrite(&p,sizeof(p),1,f);
				 }

			}
			fclose(f);
			fclose(fp);

					 if((f=fopen("temp","rb+"))==NULL)
					      {
						printf("Cannot open the file");
						getch();
						exit(1);
					      }
					 fseek(f,0,SEEK_END);
					 tsz=ftell(f);
					 n=(int)(tsz/sizeof(p));
					 for(i=0;i<(n-1);i++)
					 {
						for(a=i+1;a<n;a++)
						{
						fseek(f,i*sizeof(p),SEEK_SET);
						fread(&p,sizeof(p),1,f);
						fseek(f,a*sizeof(p),SEEK_SET);
						fread(&q,sizeof(p),1,f);
						if((p.atm-q.atm)>0)
							{
							fseek(f,i*sizeof(p),SEEK_SET);
							fwrite(&q,sizeof(p),1,f);
							fseek(f,a*sizeof(p),SEEK_SET); fflush(stdin);
							fwrite(&p,sizeof(p),1,fp);
							}
						}
					}
					rewind(f);
			while(fread(&p,sizeof(p),1,f))
			{

					print();
					getch();


			}


				system("cls");
				mainscreen();
				gotoxy(25,25);
				printf("::No Element Available::");
			fclose(f);
			getch();
			break;
		}


		default:
		{
				system("cls");
				mainscreen();
				gotoxy(22,11);
				printf("Wrong choice");gotoxy(22,13);
				 printf("Retype choice");
				goto label6;
		}
	}
	goto startofexplore;

}
void print()
{
	system("cls");
	mainscreen();
	gotoxy(15,16);
	printf("Name:");

	gotoxy(15,18);
	printf("Symbol:");

	gotoxy(15,20);
	printf("Atomic No: ");

	gotoxy(15,22);
	printf("Atomic Wt: ");

	gotoxy(15,24);
	printf("Atomic Config:");
	fflush(stdin);
	gotoxy(15,26);
	printf("Block:");

	gotoxy(15,28);
	printf("Properties:");

	gotoxy(20,16);
	printf("%s",p.name);

	gotoxy(23,18);
	printf("%s",p.sb);

	fflush(stdin);
	gotoxy(25,20);
	printf("%d",p.atm);

	fflush(stdin);
	gotoxy(25,22);
	printf("%f",p.atms);

	fflush(stdin);
	gotoxy(29,24);
	printf("%s",p.atc);

	gotoxy(21,26);
	printf("%c",p.block);

	gotoxy(26,28);
	printf("%s",p.prop);
}
