var http = require("http");
var express = require('express');
var path=require('path')
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });
app.use(urlencodedParser);
app.use(bodyParser.json())
var fs=require('fs')
 
// Running Server Details.
var server = app.listen(8082, function () {
  var host = server.address().address
  var port = server.address().port
  console.log("Example app listening at %s:%s Port", host, port)
});

 
app.get('/',function(req,res){
  res.sendFile('/home.html')
})
app.get('/road1', function (req, res) {
  var html='';
  html =`<body>
  <h1> <center> Traffic Simulator </center></h1>
        <br><br>
        <h2>Road 1</h1>
        <p>Enter the count of vehicles click add to add then into space</p>
                <form id="form1" action="/write" method="POST">
                  Truck:<input id="T1" type="number" value="0" min=0 name="T1" max="5"><br>
                  Unloaded Troller:<input id="T31" type="number" value="0" min=0 name="T31" max="5"><br>
                  Loaded Troller:<input id="T32" type="number" value="0" min=0 name="T32" max="5"><br>
                  Unloaded Tanker:<input id="T21" type="number" value="0" min=0 name="T21" max="5"><br>
                  Loaded Tanker:<input id="T22" type="number" value="0" min=0 name="T22" max="5"><br>
                  Bus:<input id="B1" type="number" value="0" min=0 name="B1" max="5"><br>
                  Car:<input id="C1" type="number" value="0" min=0 name="C1" max="15"><br>
                  Tempo:<input id="T4" type="number" value="0" min=0 name="T4" max="15"><br>
                  Erickshow:<input id="E" type="number" value="0" min=0 name="E" max="20"><br>
                  Bike:<input id="B2" type="number" value="0" min=0 name="B2" max="20"><br>
                  Cycle:<input id="C2" type="number" value="0" min=0 name="C2" max="20"><br>
                  <button type="submit">Submit</button>
          </form>
      </body>`
  res.send(html);
  //res.end(JSON.stringify(req.body,null,2))
//   var reply='';
//   reply += "Truck:" + req.body.n1+"\n";
//   reply += "utroller" + req.body.n2+"\n"; 
//   reply += "ltroller" + req.body.n3+"\n";
//   reply += "Your mobile number is" + req.body.n4+"\n";
//   res.send(reply);
});
app.post('/write',urlencodedParser,function(req,res){
    fs.writeFile("abc.txt","Road\n", (err)=>{
    if(err){
        return console.log(err);
    }
    });
    var T1=0
    // var form1=document.getElementById("form1")
    var T1=req.body.T1
    var T31=req.body.T31
    var T32=req.body.T32
    var T21=req.body.T21
    var T22=req.body.T22
    var B1=req.body.B1
    var C1=req.body.C1
    var T4=req.body.T4
    var E=req.body.E
    var B2=req.body.B2
    var C2=req.body.C2
    var space=T1*5+T31*7+T32*7+T21*6+T22*6+T4*2+B1*5+C1*2+C2*1+B2*1+E*2
    fs.appendFile("abc.txt",space,(err)=>{
      if(err)console.log(err);
      })
    if(T1!=0){
    fs.appendFile("abc.txt",T1+'\n',(err)=>{
      if(err){
        console.log(err)
      }
    })
    fs.appendFile("abc.txt",T1*5+'\n',(err)=>{
      if(err){
        console.log(err)
      }
    })
  }
    
    if(T31!=0){
      fs.appendFile("abc.txt",T31+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T31*7+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T32!=0){
      fs.appendFile("abc.txt",T32+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T32*5+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T21!=0){
      fs.appendFile("abc.txt",T21+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T21*6+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T22!=0){
      fs.appendFile("abc.txt",T22+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T22*6+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T4!=0){
      fs.appendFile("abc.txt",T4+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T4*2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(E!=0){
      fs.appendFile("abc.txt",E+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",E*2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(C1!=0){
      fs.appendFile("abc.txt",C1+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",C1*2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(B1!=0){
      fs.appendFile("abc.txt",B1+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",B1*5+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
      if(C2!=0){
        fs.appendFile("abc.txt",C2+'\n',(err)=>{
          if(err){
            console.log(err)
          }
        })
        fs.appendFile("abc.txt",C2*1+'\n',(err)=>{
          if(err){
            console.log(err)
          }
        })
        }
    
    if(B2!=0){
      fs.appendFile("abc.txt",B2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",B2*1+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
      res.redirect('./road2')
});



app.get('/road2', function (req, res) {
    var html='';
    html =`<body>
    <h1> <center> Traffic Simulator </center></h1>
        <br><br>
        <h2>Road 2</h1>
        <p>Enter the count of vehicles click add to add then into space</p>
            <form action="/append2" method="post">
                    Truck:<input id="T1" type="number" value="0" min=0 name="T1" max="5"><br>
                    Unloaded Troller:<input id="T31" type="number" value="0" min=0 name="T31" max="5"><br>
                    Loaded Troller:<input id="T32" type="number" value="0" min=0 name="T32" max="5"><br>
                    Unloaded Tanker:<input id="T21" type="number" value="0" min=0 name="T21" max="5"><br>
                    Loaded Tanker:<input id="T22" type="number" value="0" min=0 name="T22" max="5"><br>
                    Bus:<input id="B1" type="number" value="0" min=0 name="B1" max="5"><br>
                    Car:<input id="C1" type="number" value="0" min=0 name="C1" max="15"><br>
                    Tempo:<input id="T4" type="number" value="0" min=0 name="T4" max="15"><br>
                    Erickshow:<input id="E" type="number" value="0" min=0 name="E" max="20"><br>
                    Bike:<input id="B2" type="number" value="0" min=0 name="B2" max="20"><br>
                    Cycle:<input id="C2" type="number" value="0" min=0 name="C2" max="20"><br>
                    <button type="submit">Submit</button>
            </form>
        </body>`
    res.send(html);
  //   var reply='';
  //   reply += "Truck:" + req.body.n1+"\n";
  //   reply += "utroller" + req.body.n2+"\n"; 
  //   reply += "ltroller" + req.body.n3+"\n";
  //   reply += "Your mobile number is" + req.body.n4+"\n";
  //   res.send(reply);
  });
 app.post('/append2',urlencodedParser,function(req,res){
    fs.appendFile("abc.txt","Road\n",(err)=>{
    if(err)console.log(err);
    })
    // var form1=document.getElementById("form1")
    var T1=req.body.T1
    var T31=req.body.T31
    var T32=req.body.T32
    var T21=req.body.T21
    var T22=req.body.T22
    var T4=req.body.T4
    var E=req.body.E
    var C1=req.body.C1
    var B1=req.body.B1
    var C2=req.body.C2
    var B2=req.body.B2
    var space=T1*5+T31*7+T32*7+T21*6+T22*6+T4*2+B1*5+C1*2+C2*1+B2*1+E*2
    fs.appendFile("abc.txt",space,(err)=>{
      if(err)console.log(err);
      })
    if(T1!=0){
    fs.appendFile("abc.txt",T1+'\n',(err)=>{
      if(err){
        console.log(err)
      }
    })
    fs.appendFile("abc.txt",T1*5+'\n',(err)=>{
      if(err){
        console.log(err)
      }
    })
  }
    
    if(T31!=0){
      fs.appendFile("abc.txt",T31+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T31*7+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T32!=0){
      fs.appendFile("abc.txt",T32+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T32*5+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T21!=0){
      fs.appendFile("abc.txt",T21+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T21*6+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T22!=0){
      fs.appendFile("abc.txt",T22+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T22*6+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T4!=0){
      fs.appendFile("abc.txt",T4+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T4*2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(E!=0){
      fs.appendFile("abc.txt",E+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",E*2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(C1!=0){
      fs.appendFile("abc.txt",C1+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",C1*2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(B1!=0){
      fs.appendFile("abc.txt",B1+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",B1*5+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
      if(C2!=0){
        fs.appendFile("abc.txt",C2+'\n',(err)=>{
          if(err){
            console.log(err)
          }
        })
        fs.appendFile("abc.txt",C2*1+'\n',(err)=>{
          if(err){
            console.log(err)
          }
        })
        }
    
    if(B2!=0){
      fs.appendFile("abc.txt",B2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",B2*1+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
      res.redirect('/road3')
});
  app.get('/road3', function (req, res) {
    var html='';
    html =`<body>
    <h1> <center> Traffic Simulator </center></h1>
        <br><br>
        <h2>Road 3</h1>
        <p>Enter the count of vehicles click add to add then into space</p>
            <form action="/append3" method="post">
                    Truck:<input id="T1" type="number" value="0" min=0 name="T1" max="5"><br>
                    Unloaded Troller:<input id="T31" type="number" value="0" min=0 name="T31" max="5"><br>
                    Loaded Troller:<input id="T32" type="number" value="0" min=0 name="T32" max="5"><br>
                    Unloaded Tanker:<input id="T21" type="number" value="0" min=0 name="T21" max="5"><br>
                    Loaded Tanker:<input id="T22" type="number" value="0" min=0 name="T22" max="5"><br>
                    Bus:<input id="B1" type="number" value="0" min=0 name="B1" max="5"><br>
                    Car:<input id="C1" type="number" value="0" min=0 name="C1" max="15"><br>
                    Tempo:<input id="T4" type="number" value="0" min=0 name="T4" max="15"><br>
                    Erickshow:<input id="E" type="number" value="0" min=0 name="E" max="20"><br>
                    Bike:<input id="B2" type="number" value="0" min=0 name="B2" max="20"><br>
                    Cycle:<input id="C2" type="number" value="0" min=0 name="C2" max="20"><br>
                    <button type="submit">Submit</button>
            </form>
        </body>`
    res.send(html);
  });
  app.post('/append3',urlencodedParser,function(req,res){
    fs.appendFile("abc.txt","Road\n",(err)=>{
    if(err)console.log(err);
    })
    // var form1=document.getElementById("form1")
    var T1=req.body.T1
    var T31=req.body.T31
    var T32=req.body.T32
    var T21=req.body.T21
    var T22=req.body.T22
    var T4=req.body.T4
    var E=req.body.E
    var C1=req.body.C1
    var B1=req.body.B1
    var C2=req.body.C2
    var B2=req.body.B2
    var space=T1*5+T31*7+T32*7+T21*6+T22*6+T4*2+B1*5+C1*2+C2*1+B2*1+E*2
    fs.appendFile("abc.txt",space,(err)=>{
      if(err)console.log(err);
      })
    if(T1!=0){
    fs.appendFile("abc.txt",T1+'\n',(err)=>{
      if(err){
        console.log(err)
      }
    })
    fs.appendFile("abc.txt",T1*5+'\n',(err)=>{
      if(err){
        console.log(err)
      }
    })
  }
    
    if(T31!=0){
      fs.appendFile("abc.txt",T31+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T31*7+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T32!=0){
      fs.appendFile("abc.txt",T32+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T32*5+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T21!=0){
      fs.appendFile("abc.txt",T21+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T21*6+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T22!=0){
      fs.appendFile("abc.txt",T22+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T22*6+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T4!=0){
      fs.appendFile("abc.txt",T4+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T4*2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(E!=0){
      fs.appendFile("abc.txt",E+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",E*2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(C1!=0){
      fs.appendFile("abc.txt",C1+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",C1*2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(B1!=0){
      fs.appendFile("abc.txt",B1+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",B1*5+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
      if(C2!=0){
        fs.appendFile("abc.txt",C2+'\n',(err)=>{
          if(err){
            console.log(err)
          }
        })
        fs.appendFile("abc.txt",C2*1+'\n',(err)=>{
          if(err){
            console.log(err)
          }
        })
        }
    
    if(B2!=0){
      fs.appendFile("abc.txt",B2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",B2*1+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
      res.redirect('/road4')
});
  app.get('/road4', function (req, res) {
    var html='';
    html =`<body>
    <h1> <center> Traffic Simulator </center></h1>
        <br><br>
        <h2>Road 4</h1>
        <p>Enter the count of vehicles click add to add then into space</p>
            <form action="/append4" method="post">
                    Truck:<input id="T1" type="number" value="0" min=0 name="T1" max="5"><br>
                    Unloaded Troller:<input id="T31" type="number" value="0" min=0 name="T31" max="5"><br>
                    Loaded Troller:<input id="T32" type="number" value="0" min=0 name="T32" max="5"><br>
                    Unloaded Tanker:<input id="T21" type="number" value="0" min=0 name="T21" max="5"><br>
                    Loaded Tanker:<input id="T22" type="number" value="0" min=0 name="T22" max="5"><br>
                    Bus:<input id="B1" type="number" value="0" min=0 name="B1" max="5"><br>
                    Car:<input id="C1" type="number" value="0" min=0 name="C1" max="15"><br>
                    Tempo:<input id="T4" type="number" value="0" min=0 name="T4" max="15"><br>
                    Erickshow:<input id="E" type="number" value="0" min=0 name="E" max="20"><br>
                    Bike:<input id="B2" type="number" value="0" min=0 name="B2" max="20"><br>
                    Cycle:<input id="C2" type="number" value="0" min=0 name="C2" max="20"><br>
                    <button type="submit">Submit</button>
            </form>
        </body>`
    res.send(html);
  //   var reply='';
  //   reply += "Truck:" + req.body.n1+"\n";
  //   reply += "utroller" + req.body.n2+"\n"; 
  //   reply += "ltroller" + req.body.n3+"\n";
  //   reply += "Your mobile number is" + req.body.n4+"\n";
  //   res.send(reply);
  });
  app.post('/append4',urlencodedParser,function(req,res){
    fs.appendFile("abc.txt","\nRoad\n",(err)=>{
    if(err)console.log(err);
    })
    // var form1=document.getElementById("form1")
    var T1=req.body.T1
    var T31=req.body.T31
    var T32=req.body.T32
    var T21=req.body.T21
    var T22=req.body.T22
    var T4=req.body.T4
    var E=req.body.E
    var C1=req.body.C1
    var B1=req.body.B1
    var C2=req.body.C2
    var B2=req.body.B2
    var space=T1*5+T31*7+T32*7+T21*6+T22*6+T4*2+B1*5+C1*2+C2*1+B2*1+E*2
    fs.appendFile("abc.txt",space,(err)=>{
      if(err)console.log(err);
      })
    if(T1!=0){
    fs.appendFile("abc.txt",T1+'\n',(err)=>{
      if(err){
        console.log(err)
      }
    })
    fs.appendFile("abc.txt",T1*5+'\n',(err)=>{
      if(err){
        console.log(err)
      }
    })
  }
    
    if(T31!=0){
      fs.appendFile("abc.txt",T31+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T31*7+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T32!=0){
      fs.appendFile("abc.txt",T32+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T32*5+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T21!=0){
      fs.appendFile("abc.txt",T21+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T21*6+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T22!=0){
      fs.appendFile("abc.txt",T22+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T22*6+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(T4!=0){
      fs.appendFile("abc.txt",T4+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",T4*2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(E!=0){
      fs.appendFile("abc.txt",E+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",E*2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(C1!=0){
      fs.appendFile("abc.txt",C1+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",C1*2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
    if(B1!=0){
      fs.appendFile("abc.txt",B1+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",B1*5+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
    
      if(C2!=0){
        fs.appendFile("abc.txt",C2+'\n',(err)=>{
          if(err){
            console.log(err)
          }
        })
        fs.appendFile("abc.txt",C2*1+'\n',(err)=>{
          if(err){
            console.log(err)
          }
        })
        }
    
    if(B2!=0){
      fs.appendFile("abc.txt",B2+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      fs.appendFile("abc.txt",B2*1+'\n',(err)=>{
        if(err){
          console.log(err)
        }
      })
      }
      res.redirect('/output')
});
app.get('/output', urlencodedParser, function (req, res){
//   var reply='';
//   reply += "Truck:" + req.body.n1+"\n";
//   reply += "utroller" + req.body.n2+"\n"; 
//   reply += "ltroller" + req.body.n3+"\n";
//   reply += "Your mobile number is" + req.body.n4+"\n";
  res.send("Submitted");
 });
