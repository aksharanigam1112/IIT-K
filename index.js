window.onload=function(){
    var add11=document.getElementById("add11")
    var add12=document.getElementById("add12")
    var add13=document.getElementById("add13")
    var add14=document.getElementById("add14")
    var add15=document.getElementById("add15")
    var add16=document.getElementById("add16")
    var add17=document.getElementById("add17")
    var add18=document.getElementById("add18")
    var add19=document.getElementById("add19")
    var add110=document.getElementById("add110")
    var add111=document.getElementById("add111")

    var add21=document.getElementById("add21")
    var add22=document.getElementById("add22")
    var add23=document.getElementById("add23")
    var add24=document.getElementById("add24")
    var add25=document.getElementById("add25")
    var add26=document.getElementById("add26")
    var add27=document.getElementById("add27")
    var add28=document.getElementById("add28")
    var add29=document.getElementById("add29")
    var add210=document.getElementById("add210")
    var add211=document.getElementById("add211")

    var add31=document.getElementById("add31")
    var add32=document.getElementById("add32")
    var add33=document.getElementById("add33")
    var add34=document.getElementById("add34")
    var add35=document.getElementById("add35")
    var add36=document.getElementById("add36")
    var add37=document.getElementById("add37")
    var add38=document.getElementById("add38")
    var add39=document.getElementById("add39")
    var add310=document.getElementById("add310")
    var add311=document.getElementById("add311")

    var add41=document.getElementById("add41")
    var add42=document.getElementById("add42")
    var add43=document.getElementById("add43")
    var add44=document.getElementById("add44")
    var add45=document.getElementById("add45")
    var add46=document.getElementById("add46")
    var add47=document.getElementById("add47")
    var add48=document.getElementById("add48")
    var add49=document.getElementById("add49")
    var add410=document.getElementById("add410")
    var add411=document.getElementById("add411")

    var run=document.getElementById("run")
    var aT11=0;var aT131=0;var aT132=0;var aT121=0;var aT122=0; var aT14=0; var aB11=0;var aB12=0;var aC11=0;var aC12=0;var aE1=0; 
    var aT21=0;var aT231=0;var aT232=0;var aT221=0;var aT222=0; var aT24=0; var aB21=0;var aB22=0;var aC21=0;var aC22=0;var aE2=0;
    var aT31=0;var aT331=0;var aT332=0;var aT321=0;var aT322=0; var aT34=0; var aB31=0;var aB32=0;var aC31=0;var aC32=0;var aE3=0;
    var aT41=0;var aT431=0;var aT432=0;var aT421=0;var aT422=0; var aT44=0; var aB41=0;var aB42=0;var aC41=0;var aC42=0;var aE4=0;
    
    run.addEventListener('click',function(){
        
        var r1sp=document.getElementById("r1sp");
        var r2sp=document.getElementById("r2sp");
        var r3sp=document.getElementById("r3sp");
        var r4sp=document.getElementById("r4sp");
        var fs = require('fs'); 
        let data = "Road\n"
        fs.writeFile('Userinput.txt',data,(err) =>  {
            if(err) throw err;
        })
        
        // if(r1sp>=0 || r2sp>=0 || r3sp>=0 || r4sp>=0)
        // { 
        //     var fs = require('fs'); // Open the file for writing
        //     if(r1sp>=0)
        //     {
        //         let data = "Road\n"
        //         fs.writeFile('Userinput.txt',data,(err) =>  {
        //             if(err) throw err;
        //         })
        //         if(aT11)
        //         {
        //             let data = "1\n"+aT11
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }   
        //         if(aT131)
        //         {
        //             let data = "2\n"+aT131
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT132)
        //         {    
        //             let data = "3\n"+aT132
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT121)
        //         {
        //             let data = "4\n"+aT121
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT122)
        //         {
        //             let data = "5\n"+aT122
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aB11)
        //         {
        //             let data = "6\n"+aB11
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aC11)
        //         {
        //             let data = "7\n"+aC11
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aE1)
        //         {    
        //             let data = "8\n"+aE1
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT14)
        //         {    
        //             let data = "9\n"+aT14
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aB12)
        //         {    
        //             let data = "10\n"+aB12
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aC12)
        //         {    
        //             let data = "11\n"+aC12
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //     }
        //     if(r2sp>=0)
        //     {
        //         let data = "Road\n"
        //         fs.writeFile('Userinput.txt',data,(err) =>  {
        //             if(err) throw err;
        //         })
        //         if(aT21)
        //         {
        //             let data = "1\n"+aT21
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }   
        //         if(aT231)
        //         {
        //             let data = "2\n"+aT231
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT232)
        //         {    
        //             let data = "3\n"+aT232
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT221)
        //         {
        //             let data = "4\n"+aT221
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT222)
        //         {
        //             let data = "5\n"+aT222
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aB21)
        //         {
        //             let data = "6\n"+aB21
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aC21)
        //         {
        //             let data = "7\n"+aC21
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aE2)
        //         {    
        //             let data = "8\n"+aE2
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT24)
        //         {    
        //             let data = "9\n"+aT24
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aB22)
        //         {    
        //             let data = "10\n"+aB22
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aC22)
        //         {    
        //             let data = "11\n"+aC22
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //     }
        //     if(r3sp>=0)
        //     {
        //         let data = "Road\n"
        //         fs.writeFile('Userinput.txt',data,(err) =>  {
        //             if(err) throw err;
        //         })
        //         if(aT31)
        //         {
        //             let data = "1\n"+aT31
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }   
        //         if(aT331)
        //         {
        //             let data = "2\n"+aT331
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT332)
        //         {    
        //             let data = "3\n"+aT332
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT321)
        //         {
        //             let data = "4\n"+aT321
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT322)
        //         {
        //             let data = "5\n"+aT322
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aB31)
        //         {
        //             let data = "6\n"+aB31
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aC31)
        //         {
        //             let data = "7\n"+aC31
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aE3)
        //         {    
        //             let data = "8\n"+aE3
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT34)
        //         {    
        //             let data = "9\n"+aT34
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aB32)
        //         {    
        //             let data = "10\n"+aB32
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aC32)
        //         {    
        //             let data = "11\n"+aC32
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //     }
        //     if(r4sp>=0)
        //     {
        //         let data = "Road\n"
        //         fs.writeFile('Userinput.txt',data,(err) =>  {
        //             if(err) throw err;
        //         })
        //         if(aT41)
        //         {
        //             let data = "1\n"+aT41
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }   
        //         if(aT431)
        //         {
        //             let data = "2\n"+aT431
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT432)
        //         {    
        //             let data = "3\n"+aT432
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT421)
        //         {
        //             let data = "4\n"+aT421
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT422)
        //         {
        //             let data = "5\n"+aT422
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aB41)
        //         {
        //             let data = "6\n"+aB41
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aC41)
        //         {
        //             let data = "7\n"+aC41
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aE4)
        //         {    
        //             let data = "8\n"+aE4
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aT44)
        //         {    
        //             let data = "9\n"+aT44
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aB42)
        //         {    
        //             let data = "10\n"+aB42
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //         if(aC42)
        //         {    
        //             let data = "11\n"+aC12
        //             fs.writeFile('Userinput.txt',data,(err) =>  {
        //                 if(err) throw err;
        //             })
        //         }
        //     }
        // }
      
    })


    add11.addEventListener('click',function(){
        var sp=5
        var T11=document.getElementById("T11");
        var T11sp=document.getElementById("T11sp");
        var r1sp=document.getElementById("r1sp");
        T11sp.value=sp*T11.value
        if(T11.value >15 && r1sp.value-T11sp.value<0){
            T11.value=0
            T11sp.value=0
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else
        {   
            aT11+=parseInt(T11.value)
            r1sp.value-=T11sp.value
        }
    })
    add21.addEventListener('click',function(){
        var sp=5
        var T21=document.getElementById("T21");
        var T21sp=document.getElementById("T21sp");
        var r2sp=document.getElementById("r2sp");
        T21sp.value=sp*T21.value;
        if(T21.value>15 && r2sp.value-T21sp.value<0){
            T21.value=0;
            T21sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units");
        }
        else{
            aT21+=parseInt(T21.value);
            r2sp.value-=T21sp.value;
        }
    })
    add31.addEventListener('click',function(){
        var sp=5
        var T31=document.getElementById("T31");
        var T31sp=document.getElementById("T31sp");
        var r3sp=document.getElementById("r3sp");
        T31sp.value=sp*T31.value;
        if(T31.value > 15 && r3sp.value-T31sp.value<0){
            T31.value=0;
            T31sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units");
        }
        else{
        aT31+=parseInt(T31.value);
        r3sp.value-=T31sp.value;
        }
    })
    add41.addEventListener('click',function(){
        var sp=5
        var T41=document.getElementById("T41");
        var T41sp=document.getElementById("T41sp");
        var r4sp=document.getElementById("r4sp");
        T41sp.value=sp*T41.value;
        if(T41.value > 15 && r4sp.value-T41sp.value<0){
            T41.value=0;
            T41sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units");
        }
        else{
        aT41+=parseInt(T41.value);
        r4sp.value-=T41sp.value;
        }
    })
    add12.addEventListener('click',function(){
        var sp=7
        var T131=document.getElementById("T131");
        var T131sp=document.getElementById("T131sp");
        var r1sp=document.getElementById("r1sp");
        T131sp.value=sp*T131.value
        if(T131.value > 10 && r1sp.value-T131sp.value<0){
            T131.value=0;
            T131sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT131+=parseInt(T131.value)
        r1sp.value-=T131sp.value
        }
    })
    add22.addEventListener('click',function(){
        var sp=7
        var T231=document.getElementById("T231");
        var T231sp=document.getElementById("T231sp");
        var r2sp=document.getElementById("r2sp");
        T231sp.value=sp*T231.value;
        if(T231.value > 10 && r2sp.value-T231sp.value<0){
            T231.value=0;
            T231sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units");
        }
        else{
        aT231+=parseInt(T231.value);
        r2sp.value-=T231sp.value;
        }
    })
    add32.addEventListener('click',function(){
        var sp=7
        var T331=document.getElementById("T331");
        var T331sp=document.getElementById("T331sp");
        var r3sp=document.getElementById("r3sp");
        T331sp.value=sp*T331.value;
        if(T331.value>10 && r3sp.value-T331sp.value<0){
            T331.value=0;
            T331sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units");
        }
        else{  
        aT331+=parseInt(T331.value);
        r3sp.value-=T331sp.value;
        }
    })
    add42.addEventListener('click',function(){
        var sp=7
        var T431=document.getElementById("T431");
        var T431sp=document.getElementById("T431sp");
        var r4sp=document.getElementById("r4sp");
        T431sp.value=sp*T431.value;
        if(T431.value>10 && r4sp.value-T431sp.value<0){
            T431.value=0;
            T431sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units");
        }
        else{
        aT431+=parseInt(T431.value);
        r4sp.value-=T431sp.value;
        }
    })


    // All Remaining Vehicles of Road 1

    add13.addEventListener('click',function(){
        var sp=7
        var T132=document.getElementById("T132");
        var T132sp=document.getElementById("T132sp");
        var r1sp=document.getElementById("r1sp");
        T132sp.value=sp*T132.value
        if(r1sp.value-T132sp.value<0 && T132.value>10){
            T132.value=0;
            T132sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT132+=parseInt(T132.value)
        r1sp.value-=T132sp.value
        }
    })

    add14.addEventListener('click',function(){
        var sp=6
        var T121=document.getElementById("T121");
        var T121sp=document.getElementById("T121sp");
        var r1sp=document.getElementById("r1sp");
        T121sp.value=sp*T121.value
        if(r1sp.value-T121sp.value<0 && T121.value >12){
            T121.value=0;
            T121sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT121+=parseInt(T121.value)
        r1sp.value-=T121sp.value
        }
    })

    add15.addEventListener('click',function(){
        var sp=6
        var T122=document.getElementById("T122");
        var T122sp=document.getElementById("T122sp");
        var r1sp=document.getElementById("r1sp");
        T122sp.value=sp*T122.value
        if(r1sp.value-T122sp.value<0 && T122.value > 12){
            T122.value=0;
            T122sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT122+=parseInt(T122.value)
        r1sp.value-=T122sp.value
        }
    })

    add16.addEventListener('click',function(){
        var sp=5
        var B11=document.getElementById("B11");
        var B11sp=document.getElementById("B11sp");
        var r1sp=document.getElementById("r1sp");
        B11sp.value=sp*B11.value
        if(r1sp.value-B11sp.value<0 && B11.value>15){
            B11.value=0;
            B11sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aB11+=parseInt(B11.value)
        r1sp.value-=B11sp.value
        }
    })

    add17.addEventListener('click',function(){
        var sp=2
        var C11=document.getElementById("C11");
        var C11sp=document.getElementById("C11sp");
        var r1sp=document.getElementById("r1sp");
        C11sp.value=sp*C11.value
        if(r1sp.value-C11sp.value<0 && C11.value > 37){
            C11.value=0;
            C11sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aC11+=parseInt(C11.value)
        r1sp.value-=C11sp.value
        }
    })

    add18.addEventListener('click',function(){
        var sp=2
        var T14=document.getElementById("T14");
        var T14sp=document.getElementById("T14sp");
        var r1sp=document.getElementById("r1sp");
        T14sp.value=sp*T14.value
        if(r1sp.value-T14sp.value<0 && T14.value > 37){
            T14.value=0;
            T14sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT14+=parseInt(T14.value)
        r1sp.value-=T14sp.value
        }
    })

    add19.addEventListener('click',function(){
        var sp=2
        var E1=document.getElementById("E1");
        var E1sp=document.getElementById("E1sp");
        var r1sp=document.getElementById("r1sp");
        E1sp.value=sp*E1.value
        if(r1sp.value-E1sp.value<0 && E1.value > 37){
            E1.value=0;
            E1sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aE1+=parseInt(E1.value)
        r1sp.value-=E1sp.value
        }
    })

    add110.addEventListener('click',function(){
        var sp=1
        var B12=document.getElementById("B12");
        var B12sp=document.getElementById("B12sp");
        var r1sp=document.getElementById("r1sp");
        B12sp.value=sp*B12.value
        if(r1sp.value-B12sp.value<0 && B12.value>75){
            B12.value=0;
            B12sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aB12+=parseInt(B12.value)
        r1sp.value-=B12sp.value
        }
    })

    add111.addEventListener('click',function(){
        var sp=1
        var C12=document.getElementById("C12");
        var C12sp=document.getElementById("C12sp");
        var r1sp=document.getElementById("r1sp");
        C12sp.value=sp*C12.value
        if(r1sp.value-C12sp.value<0 && C12.value>75){
            C12.value=0;
            C12sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aC12+=parseInt(C12.value)
        r1sp.value-=C12sp.value
        }
    })

    // All rem vehicles of Road 2

    add23.addEventListener('click',function(){
        var sp=7
        var T232=document.getElementById("T232");
        var T232sp=document.getElementById("T232sp");
        var r2sp=document.getElementById("r2sp");
        T232sp.value=sp*T232.value
        if(r2sp.value-T232sp.value<0 && T232.value>10){
            T232.value=0;
            T232sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT232+=parseInt(T232.value)
        r2sp.value-=T232sp.value
        }
    })

    add24.addEventListener('click',function(){
        var sp=6
        var T221=document.getElementById("T221");
        var T221sp=document.getElementById("T221sp");
        var r2sp=document.getElementById("r2sp");
        T221sp.value=sp*T221.value
        if(r2sp.value-T221sp.value<0 && T221.value>12){
            T221.value=0;
            T221sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT221+=parseInt(T221.value)
        r2sp.value-=T221sp.value
        }
    })

    add25.addEventListener('click',function(){
        var sp=6
        var T222=document.getElementById("T222");
        var T222sp=document.getElementById("T222sp");
        var r2sp=document.getElementById("r2sp");
        T222sp.value=sp*T222.value
        if(r2sp.value-T222sp.value<0 &&T222.value>12){
            T222.value=0;
            T222sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT222+=parseInt(T222.value)
        r2sp.value-=T222sp.value
        }
    })

    add26.addEventListener('click',function(){
        var sp=5
        var B21=document.getElementById("B21");
        var B21sp=document.getElementById("B21sp");
        var r2sp=document.getElementById("r2sp");
        B21sp.value=sp*B21.value
        if(r2sp.value-B21sp.value<0 && B21.value>15){
            B21.value=0;
            B21sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aB21+=parseInt(B21.value)
        r2sp.value-=B21sp.value
        }
    })

    add27.addEventListener('click',function(){
        var sp=2
        var C21=document.getElementById("C21");
        var C21sp=document.getElementById("C21sp");
        var r2sp=document.getElementById("r2sp");
        C21sp.value=sp*C21.value
        if(r2sp.value-C21sp.value<0 && C21.value>37){
            C21.value=0;
            C21sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aC21+=parseInt(C21.value)
        r2sp.value-=C21sp.value
        }
    })

    add28.addEventListener('click',function(){
        var sp=2
        var T24=document.getElementById("T24");
        var T24sp=document.getElementById("T24sp");
        var r2sp=document.getElementById("r2sp");
        T24sp.value=sp*T24.value
        if(r2sp.value-T24sp.value<0 && T24.value>37){
            T24.value=0;
            T24sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT24+=parseInt(T24.value)
        r2sp.value-=T24sp.value
        }
    })

    add29.addEventListener('click',function(){
        var sp=2
        var E2=document.getElementById("E2");
        var E2sp=document.getElementById("E2sp");
        var r2sp=document.getElementById("r2sp");
        E2sp.value=sp*E2.value
        if(r2sp.value-E2sp.value<0 && E2.value>37){
            E2.value=0;
            E2sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aE2+=parseInt(E2.value)
        r2sp.value-=E2sp.value
        }
    })

    add210.addEventListener('click',function(){
        var sp=1
        var B22=document.getElementById("B22");
        var B22sp=document.getElementById("B22sp");
        var r2sp=document.getElementById("r2sp");
        B22sp.value=sp*B22.value
        if(r2sp.value-B22sp.value<0 && B22.value>75){
            B22.value=0;
            B22sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aB22+=parseInt(B22.value)
        r2sp.value-=B22sp.value
        }
    })

    add211.addEventListener('click',function(){
        var sp=1
        var C22=document.getElementById("C22");
        var C22sp=document.getElementById("C22sp");
        var r2sp=document.getElementById("r2sp");
        C22sp.value=sp*C22.value
        if(r2sp.value-C22sp.value<0 && C22.value>75){
            C22.value=0;
            C22sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aC22+=parseInt(C22.value)
        r2sp.value-=C22sp.value
        }
    })
    
    // All rem vehicles of Road 3

    add33.addEventListener('click',function(){
        var sp=7
        var T332=document.getElementById("T332");
        var T332sp=document.getElementById("T332sp");
        var r3sp=document.getElementById("r3sp");
        T332sp.value=sp*T332.value
        if(r3sp.value-T332sp.value<0 && T332.value>10){
            T332.value=0;
            T332sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT332+=parseInt(T332.value)
        r3sp.value-=T332sp.value
        }
    })

    add34.addEventListener('click',function(){
        var sp=6
        var T321=document.getElementById("T321");
        var T321sp=document.getElementById("T321sp");
        var r3sp=document.getElementById("r3sp");
        T321sp.value=sp*T321.value
        if(r3sp.value-T321sp.value<0 && T321.value>12){
            T321.value=0;
            T321sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT321+=parseInt(T321.value)
        r3sp.value-=T321sp.value
        }
    })

    add35.addEventListener('click',function(){
        var sp=6
        var T322=document.getElementById("T322");
        var T322sp=document.getElementById("T322sp");
        var r3sp=document.getElementById("r3sp");
        T322sp.value=sp*T322.value
        if(r3sp.value-T322sp.value<0 && T322.value>12){
            T322.value=0;
            T322sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT322+=parseInt(T322.value)
        r3sp.value-=T322sp.value
        }
    })

    add36.addEventListener('click',function(){
        var sp=5
        var B31=document.getElementById("B31");
        var B31sp=document.getElementById("B31sp");
        var r3sp=document.getElementById("r3sp");
        B31sp.value=sp*B31.value
        if(r3sp.value-B31sp.value<0 && B31.value>15){
            B31.value=0;
            B31sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aB31+=parseInt(B31.value)
        r3sp.value-=B31sp.value
        }
    })

    add37.addEventListener('click',function(){
        var sp=2
        var C31=document.getElementById("C31");
        var C31sp=document.getElementById("C31sp");
        var r3sp=document.getElementById("r3sp");
        C31sp.value=sp*C31.value
        if(r3sp.value-C31sp.value<0 && C31.value>37){
            C31.value=0;
            C31sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aC31+=parseInt(C31.value)
        r3sp.value-=C31sp.value
        }
    })

    add38.addEventListener('click',function(){
        var sp=2
        var T34=document.getElementById("T34");
        var T34sp=document.getElementById("T34sp");
        var r3sp=document.getElementById("r3sp");
        T34sp.value=sp*T34.value
        if(r3sp.value-T34sp.value<0 && T34.value>37){
            T34.value=0;
            T34sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT34+=parseInt(T34.value)
        r3sp.value-=T34sp.value
        }
    })

    add39.addEventListener('click',function(){
        var sp=2
        var E3=document.getElementById("E3");
        var E3sp=document.getElementById("E3sp");
        var r3sp=document.getElementById("r3sp");
        E3sp.value=sp*E3.value
        if(r3sp.value-E3sp.value<0 && E3.value>37){
            E3.value=0;
            E3sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aE3+=parseInt(E3.value)
        r3sp.value-=E3sp.value
        }
    })

    add310.addEventListener('click',function(){
        var sp=1
        var B32=document.getElementById("B32");
        var B32sp=document.getElementById("B32sp");
        var r3sp=document.getElementById("r3sp");
        B32sp.value=sp*B32.value
        if(r3sp.value-B32sp.value<0 && B32.value>75){
            B32.value=0;
            B32sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aB32+=parseInt(B32.value)
        r3sp.value-=B32sp.value
        }
    })

    add311.addEventListener('click',function(){
        var sp=1
        var C32=document.getElementById("C32");
        var C32sp=document.getElementById("C32sp");
        var r3sp=document.getElementById("r3sp");
        C32sp.value=sp*C32.value
        if(r3sp.value-C32sp.value<0 && C32.value>75){
            C32.value=0;
            C32sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aC32+=parseInt(C32.value)
        r3sp.value-=C32sp.value
        }
    })

    //All rem vehicles of road 4

    add43.addEventListener('click',function(){
        var sp=7
        var T432=document.getElementById("T432");
        var T432sp=document.getElementById("T432sp");
        var r4sp=document.getElementById("r4sp");
        T432sp.value=sp*T432.value
        if(r4sp.value-T432sp.value<0 && T432.value>10){
            T432.value=0;
            T432sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT432+=parseInt(T432.value)
        r4sp.value-=T432sp.value
        }
    })

    add44.addEventListener('click',function(){
        var sp=6
        var T421=document.getElementById("T421");
        var T421sp=document.getElementById("T421sp");
        var r4sp=document.getElementById("r4sp");
        T421sp.value=sp*T421.value
        if(r4sp.value-T421sp.value<0 &&T421.value>12){
            T421.value=0;
            T421sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT421+=parseInt(T421.value)
        r4sp.value-=T421sp.value
        }
    })

    add45.addEventListener('click',function(){
        var sp=6
        var T422=document.getElementById("T422");
        var T422sp=document.getElementById("T422sp");
        var r4sp=document.getElementById("r4sp");
        T422sp.value=sp*T422.value
        if(r4sp.value-T422sp.value<0 && T422.value>12){
            T422.value=0;
            T422sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT422+=parseInt(T422.value)
        r4sp.value-=T422sp.value
        }
    })

    add46.addEventListener('click',function(){
        var sp=5
        var B41=document.getElementById("B41");
        var B41sp=document.getElementById("B41sp");
        var r4sp=document.getElementById("r4sp");
        B41sp.value=sp*B41.value
        if(r4sp.value-B41sp.value<0 && B41.value>15){
            B41.value=0;
            B41sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aB41+=parseInt(B41.value)
        r4sp.value-=B41sp.value
        }
    })

    add47.addEventListener('click',function(){
        var sp=2
        var C41=document.getElementById("C41");
        var C41sp=document.getElementById("C41sp");
        var r4sp=document.getElementById("r4sp");
        C41sp.value=sp*C41.value
        if(r4sp.value-C41sp.value<0 && C41.value>37){
            C41.value=0;
            C41sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aC41+=parseInt(C41.value)
        r4sp.value-=C41sp.value
        }
    })

    add48.addEventListener('click',function(){
        var sp=2
        var T44=document.getElementById("T44");
        var T44sp=document.getElementById("T44sp");
        var r4sp=document.getElementById("r4sp");
        T44sp.value=sp*T44.value
        if(r4sp.value-T44sp.value<0 && T44.value>37){
            T44.value=0;
            T44sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aT44+=parseInt(T44.value)
        r4sp.value-=T44sp.value
        }
    })

    add49.addEventListener('click',function(){
        var sp=2
        var E4=document.getElementById("E4");
        var E4sp=document.getElementById("E4sp");
        var r4sp=document.getElementById("r4sp");
        E4sp.value=sp*E4.value
        if(r4sp.value-E4sp.value<0 && E4.value>37){
            E4.value=0;
            E4sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aE4+=parseInt(E4.value)
        r4sp.value-=E4sp.value
        }
    })

    add410.addEventListener('click',function(){
        var sp=1
        var B42=document.getElementById("B42");
        var B42sp=document.getElementById("B42sp");
        var r4sp=document.getElementById("r4sp");
        B42sp.value=sp*B42.value
        if(r4sp.value-B42sp.value<0 && B42.value>75){
            B42.value=0;
            B42sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aB42+=parseInt(B42.value)
        r4sp.value-=B42sp.value
        }
    })

    add411.addEventListener('click',function(){
        var sp=1
        var C42=document.getElementById("C42");
        var C42sp=document.getElementById("C42sp");
        var r4sp=document.getElementById("r4sp");
        C42sp.value=sp*C42.value
        if(r4sp.value-C42sp.value<0 && C42.value>75){
            C42.value=0;
            C42sp.value=0;
            alert("\nSpace of a road cannot exceed 75 units")
        }
        else{
        aC42+=parseInt(C42.value)
        r4sp.value-=C42sp.value
        }
    })

}