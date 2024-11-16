from flet import*
import string
from passwordmanager import*
n=0
def main(page:Page):
    dn=Ref[TextField]()
    pas=Ref[TextField]()
    maspas=Ref[TextField]()
    masbtn=Ref[ElevatedButton]()
    result=Ref[Text]()
    seetxt=Ref[Text]()
    seepastxt=Ref[Text]()
    app_bar=Ref[AppBar]()
    lock=Ref[Icon]()
    icon_btn=Ref[IconButton]()
    agp=Ref[ElevatedButton]()
    ogp=Ref[ElevatedButton]()
    words=Ref[TextField]()
    number=Ref[TextField]()
    symbol=Ref[TextField]()
    length=Ref[TextField]()
    gene=Ref[ElevatedButton]()
    et=Ref[ExpansionTile]()
    dlg=Ref[AlertDialog]()
    delsb=Ref[SnackBar]()
    ico=Ref[IconButton]()
    de=decryption()
    temp=Column()
    arr=[]

    page.snack_bar=SnackBar(
        content=Text(),
        bgcolor="black",
        duration=2000
        )

    te=[]
    def delete(e):
        te.append(e.control.data)
        dlg.current.open=True
        dlg.current.content=Text(f"Do Really Want To Delete {arr[te[0]]}",size=22,weight=FontWeight.W_700)
        if e.control.data=="yes":
            t=deletion(arr[te[0]])
            temp.controls.pop(te[0])
            temp.controls.insert(te[0],Text("",visible=False))
            te.clear()
            dlg.current.open=False
            delsb.current.content=Text(t,color=colors.RED_600,size=25,weight=FontWeight.W_700)
            delsb.current.open=True
        page.update()
    def dismiss(e):
        dlg.current.open=False
        te.clear()
        page.update()
    
    def copy(e):
        page.set_clipboard(e.control.data)
        delsb.current.content=Text(value="Copied Successfully",color=colors.GREEN_600,size=25,weight=FontWeight.W_700)
        delsb.current.open=True
        page.update()
    
    def openpass(e):
        global n
        for i in de.keys():
            temp.controls.append(ExpansionTile(ref=et,title=Text(ref=seetxt,value=i,color="pink",size=25,weight=FontWeight.W_700),trailing=IconButton(ref=ico,icon=icons.DELETE,icon_color=colors.RED_500,on_click=delete,data=n)))
            n+=1
            arr.append(i)
            for j in de[i]:
                et.current.controls.append(ListTile(title=Text(ref=seepastxt,value=j,text_align=TextAlign.CENTER,color="yellow",size=22,weight=FontWeight.W_700),trailing=IconButton(icon=icons.COPY,on_click=copy,data=j,icon_color="black"),bgcolor=colors.GREY))
        page.update()
        return temp
    openpass(page)
    
    def seepass(e):
        t=mainpass(maspas.current.value)
        if t==True:
            maspas.current.value=""
            page.go("/seepassword")
        else:
            maspas.current.value=""
            maspas.current.focus()
            bs.open=False
            if t=="successfully created":
                page.snack_bar.content=Text(t,color=colors.GREEN_600,size=25,weight=FontWeight.W_700)
            else:
                page.snack_bar.content=Text(t,color=colors.RED_600,size=25,weight=FontWeight.W_700)
            page.snack_bar.open=True
        page.update()

    bs=BottomSheet(Container(
            Column([
                TextField(ref=maspas,label="Enter Your Master Password",border_radius=60,text_align="center",text_style=TextStyle(weight=FontWeight.W_700,size=20,color="black"),label_style=TextStyle(weight=FontWeight.W_700,color="black",size=20),width=350,autofocus=True,on_submit=lambda e:masbtn.current.focus(),password=True,can_reveal_password=True,bgcolor="cyan",border_color="white"),
                Divider(opacity=0),
                ElevatedButton(ref=masbtn,text="Sumbit",on_click=seepass)
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
            height=200,
            padding=10,
            border_radius=60
        ),
        bgcolor="yellow",dismissible=True
    )


    def bottombar(e):
        bs.open=True
        page.update()

    def openall(e):
        icon_btn.current.on_click=createown
        agp.current.visible=False
        ogp.current.visible=False
        words.current.visible=True
        number.current.visible=True
        symbol.current.visible=True
        length.current.visible=True
        gene.current.visible=True
        page.update()

    def createown(e):
        if words.current.value=="" or number.current.value=="" or symbol.current.value=="" or length.current.value=="":
            result.current.value="Enter A Valid Input"
            result.current.color=colors.RED_900
        else:
            icon_btn.current.icon_color=random.choice(["red","blue","pink","black","orange","purple","yellow"])
            result.current.color=random.choice(["red","blue","pink","black","orange","purple","yellow"])
            t=generatepass(words.current.value.lower(),number.current.value,symbol.current.value,int(length.current.value))
            result.current.value=t
        page.update()


    def gen(e):
        ogp.current.visible=False
        icon_btn.current.icon_color=random.choice(["red","blue","pink","black","orange","purple","yellow"])
        t=generatepass(string.ascii_lowercase,string.digits,"!@#$%&",9)
        result.current.color=random.choice(["red","blue","pink","black","orange","purple","yellow"])
        result.current.value=t
        page.update()

    def storepassword(e):
        if dn.current.value!="" and pas.current.value!="":
            lock.current.name="lock"
            lock.current.color=colors.GREEN_900
            t=storepasss(dn.current.value.title(),pas.current.value)
            temp.controls.append(ExpansionTile(ref=et,title=Text(ref=seetxt,value=dn.current.value,color="pink",size=25,weight=FontWeight.W_700),trailing=IconButton(ref=ico,icon=icons.DELETE,icon_color=colors.RED_500,data=n,on_click=delete)))
            et.current.controls.append(ListTile(title=Text(ref=seepastxt,value=pas.current.value,text_align=TextAlign.CENTER,color="yellow",size=22,weight=FontWeight.W_700),trailing=IconButton(icon=icons.COPY,on_click=copy,data=pas.current.value,icon_color="black")))
            arr.append(dn.current.value.title())
            result.current.color=colors.GREEN_800
            result.current.value=t
            dn.current.value=""
            pas.current.value=""
                      
        else:
            
            lock.current.name="lock_open"
            lock.current.color=colors.RED_700
            result.current.color=colors.RED_500
            result.current.value="The Domain Name Or Passsword Could Not Be Empty"    
        page.update()

    def nextbtn(e):
        pas.current.focus()

    def change(e):
        page.views.clear()
        page.views.append(
            View(
                route="/",
                appbar=AppBar(ref=app_bar,title=Text("Password Manager"),center_title=True,actions=[IconButton(icon=icons.PASSWORD,tooltip="See Your Passwords",on_click=bottombar)]),
                controls=[
                Image(src="image2.png",width=400,height=400),
                ElevatedButton(text="Store Password",icon=icons.LOCK,on_click=lambda e:page.go("/store")),
                Divider(opacity=0),
                ElevatedButton(text="Create Password",icon=icons.CREATE,on_click=lambda e:page.go("/generate"))],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                bgcolor="grey",
                scroll=ScrollMode.ALWAYS,
                auto_scroll=True   
            )
        )
        if page.route=="/store":
            page.views.append(
                View(
                    "/store",
                    appbar=AppBar(ref=app_bar,leading=IconButton(icon=icons.ARROW_BACK_ROUNDED,tooltip="go to home page",on_click=lambda e:page.go("/")),title=Text(value="Storing Password"),center_title=True,actions=[Icon(icons.LOCK)]),
                    controls=[
                    Icon(ref=lock,name="lock_open",color=colors.RED_700,size=100),
                    Divider(opacity=0),
                    TextField(ref=dn,text_style=TextStyle(weight=FontWeight.W_700,size=20),color="black",label="DomainName",label_style=TextStyle(weight=FontWeight.W_700,color="black",size=20),width=350,border_radius=50,text_align="center",autofocus=True,on_submit=nextbtn,capitalization=TextCapitalization.WORDS),
                    Divider(opacity=0),
                    TextField(ref=pas,text_style=TextStyle(weight=FontWeight.W_700,size=20),color="black",label="Password",width=350,border_radius=50,text_align="center",label_style=TextStyle(weight=FontWeight.W_700,color="black",size=20),on_submit=storepassword),
                    Divider(opacity=0),
                    ElevatedButton(text="Sumbit",on_click=storepassword),
                    Text(ref=result,color="black",weight=FontWeight.W_900,size=30,text_align=TextAlign.CENTER),
                ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor="grey",
                    scroll=ScrollMode.ALWAYS
                )
            )

        elif page.route=="/generate":
            page.views.append(
                View(
                    route="/generate",
                    appbar=AppBar(ref=app_bar,leading=IconButton(icon=icons.ARROW_BACK_ROUNDED,tooltip="go to home page",on_click=lambda e:page.go("/")),title=Text(value="Generating Password"),center_title=True,actions=[Icon(icons.CREATE)]),
                    controls=[
                    IconButton(ref=icon_btn,icon="create",icon_size=120,icon_color=random.choice(["red","blue","pink","black","orange","purple","yellow"]),on_click=gen,highlight_color="grey"),
                    Divider(opacity=0),
                    ElevatedButton(ref=agp,text="Generate Password",on_click=gen),
                    Divider(opacity=0),
                    ElevatedButton(ref=ogp,text="Generate password by own",on_click=openall),
                    TextField(ref=words,text_style=TextStyle(weight=FontWeight.W_700,size=20),color="black",label="Words",hint_text="Eg-abcd...",hint_style=TextStyle(color="black"),width=350,border_radius=50,text_align="center",label_style=TextStyle(weight=FontWeight.W_700,color="black",size=20),autofocus=True,on_submit=lambda e:number.current.focus(),visible=False),
                    TextField(ref=number,keyboard_type=KeyboardType.NUMBER,text_style=TextStyle(weight=FontWeight.W_700,size=20),color="black",label="Numbers",hint_text="Eg-1234...",hint_style=TextStyle(color="black"),width=350,border_radius=50,text_align="center",label_style=TextStyle(weight=FontWeight.W_700,color="black",size=20),on_submit=lambda e:symbol.current.focus(),visible=False),
                    TextField(ref=symbol,text_style=TextStyle(weight=FontWeight.W_700,size=20),color="black",label="Symbols",hint_text="Eg-@#&%...",hint_style=TextStyle(color="black"),width=350,border_radius=50,text_align="center",label_style=TextStyle(weight=FontWeight.W_700,color="black",size=20),on_submit=lambda e:length.current.focus(),visible=False),
                    TextField(ref=length,key=KeyboardType.NUMBER,text_style=TextStyle(weight=FontWeight.W_700,size=20),color="black",label="Length",hint_text="Eg-8..",hint_style=TextStyle(color="black"),width=350,border_radius=50,text_align="center",label_style=TextStyle(weight=FontWeight.W_700,color="black",size=20),on_submit=lambda e:gene.current.focus(),visible=False),
                    ElevatedButton(ref=gene,text="Generate",on_click=createown,visible=False),
                    Text(ref=result,color="red",size=40,weight=FontWeight.W_700,text_align="center")
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,bgcolor="grey",
                    scroll=ScrollMode.ALWAYS   
                )  
            )
        elif page.route=="/seepassword":
            page.views.append(View(
                route="/seepassword",
                appbar=AppBar(ref=app_bar,leading=IconButton(icon=icons.ARROW_BACK_ROUNDED,tooltip="go to home age",on_click=lambda e:page.go("/")),title=Text(value="Opening Password"),center_title=True,actions=[Icon(icons.LOCK)]),
                controls=[temp,SnackBar(ref=delsb,content=Text(),bgcolor="black",duration=2000),AlertDialog(ref=dlg,modal=True,title=Text("Please Confirm"),content=[],actions=[TextButton(text="Confirm",on_click=delete,data="yes"),TextButton(text="No",on_click=dismiss,data="no")])],
                bgcolor="grey",
                scroll=ScrollMode.ALWAYS
            ))
            
        page.update()
    page.overlay.append(bs)
    page.on_route_change=change
    page.go(page.route)
app(target=main)