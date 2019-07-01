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
        if(r1sp>=0 && r2sp>=0 && r3sp>=0 && r4sp>=0){ 
        //yaha file right ka code aayega
        }
    })

    add11.addEventListener('click',function(){
        var sp=5
        var T11=document.getElementById("T11");
        var T11sp=document.getElementById("T11sp");
        var r1sp=document.getElementById("r1sp");
        T11sp.value=sp*T11.value
        if(r1sp-T11sp.value<0){
            T11.value=0;
            T11sp.value=0;
            alert("space of a road cannot exceed 75 units")
        }
        else{
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
        if(r2sp-T21sp.value<0){
            T21.value=0;
            T21sp.value=0;
            alert("space of a road cannot exceed 75 units");
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
        if(r3sp-T31sp.value<0){
            T31.value=0;
            T31sp.value=0;
            alert("space of a road cannot exceed 75 units");
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
        if(r4sp-T41sp.value<0){
            T41.value=0;
            T41sp.value=0;
            alert("space of a road cannot exceed 75 units");
        }
        else{
        aT41+=parseInt(T41.value);
        r4sp.value-=T41sp.value;
        }
    })
    add12.addEventListener('click',function(){
        var sp=7
        var T12=document.getElementById("T12");
        var T12sp=document.getElementById("T12sp");
        var r1sp=document.getElementById("r1sp");
        T12sp.value=sp*T12.value
        if(r1sp-T12sp.value<0){
            T12.value=0;
            T12sp.value=0;
            alert("space of a road cannot exceed 75 units")
        }
        else{
        aT12+=parseInt(T12.value)
        r1sp.value-=T12sp.value
        }
    })
    add22.addEventListener('click',function(){
        var sp=7
        var T22=document.getElementById("T22");
        var T22sp=document.getElementById("T22sp");
        var r2sp=document.getElementById("r2sp");
        T22sp.value=sp*T22.value;
        if(r2sp-T22sp.value<0){
            T22.value=0;
            T22sp.value=0;
            alert("space of a road cannot exceed 75 units");
        }
        else{
        aT22+=parseInt(T22.value);
        r2sp.value-=T22sp.value;
        }
    })
    add32.addEventListener('click',function(){
        var sp=7
        var T32=document.getElementById("T32");
        var T32sp=document.getElementById("T32sp");
        var r3sp=document.getElementById("r3sp");
        T32sp.value=sp*T32.value;
        if(r3sp-T32sp.value<0){
            T32.value=0;
            T32sp.value=0;
            alert("space of a road cannot exceed 75 units");
        }
        else{
        aT32+=parseInt(T32.value);
        r3sp.value-=T31sp.value;
        }
    })
    add42.addEventListener('click',function(){
        var sp=7
        var T42=document.getElementById("T42");
        var T42sp=document.getElementById("T42sp");
        var r4sp=document.getElementById("r4sp");
        T42sp.value=sp*T42.value;
        if(r4sp-T42sp.value<0){
            T42.value=0;
            T42sp.value=0;
            alert("space of a road cannot exceed 75 units");
        }
        else{
        aT42+=parseInt(T42.value);
        r4sp.value-=T42sp.value;
        }
    })
}