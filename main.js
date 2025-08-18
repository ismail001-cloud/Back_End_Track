// to change the nav bar on scroll

window.addEventListener('scroll', () => {
    document.querySelector('nav').classList.toggle
    ('window-scroll', window.scrollY > 0)
})


//--=================== JAVASCRIPT FOR PORTFOLIO====================

    var tablinks = document.getElementsByClassName("tab-links");
    var tabcontents = document.getElementsByClassName("tab-contents");

    function opentab(tabname){
        for(tablink of tablinks){
            tablink.classList.remove("active-link");
        }

        for(tabcontent of tabcontents){
            tabcontent.classList.remove("active-tab");  
        }
        
        event.currentTarget.classList.add("active-link");
        document.getElementById(tabname).classList.add("active-tab");
    }


//--=================== JAVASCRIPT FOR PRODUCTS GAlLERY====================

    var ProductImg = document.getElementById("ProductImg");
    var SmallImg = document.getElementsByClassName("small-img");
        
        SmallImg[0].onclick = function() 
        {
            ProductImg.src = SmallImg[0].src;
        }    

        SmallImg[1].onclick = function() 
        {
            ProductImg.src = SmallImg[1].src;
        }

        SmallImg[2].onclick = function() 
        {
            ProductImg.src = SmallImg[2].src;
        }
        
        SmallImg[3].onclick = function() 
        {
            ProductImg.src = SmallImg[3].src;
        }


    var ProductImg1 = document.getElementById("ProductImg1");
    var SmallImg1 = document.getElementsByClassName("small-img1");
        
        SmallImg1[0].onclick = function() 
        {
            ProductImg1.src = SmallImg1[0].src;
        }

        SmallImg1[1].onclick = function() 
        {
            ProductImg1.src = SmallImg1[1].src;
        }

        SmallImg1[2].onclick = function() 
        {
            ProductImg1.src = SmallImg1[2].src;
        }
        
        SmallImg1[3].onclick = function() 
        {
            ProductImg1.src = SmallImg1[3].src;
        }


        var ProductImg2 = document.getElementById("ProductImg2");
        var SmallImg2 = document.getElementsByClassName("small-img2");
            
            SmallImg2[0].onclick = function() 
            {
                ProductImg2.src = SmallImg2[0].src;
            }
    
            SmallImg2[1].onclick = function() 
            {
                ProductImg2.src = SmallImg2[1].src;
            }
    
            SmallImg2[2].onclick = function() 
            {
                ProductImg2.src = SmallImg2[2].src;
            }
            
            SmallImg2[3].onclick = function() 
            {
                ProductImg2.src = SmallImg2[3].src;
            }
    

            var ProductImg3 = document.getElementById("ProductImg3");
            var SmallImg3 = document.getElementsByClassName("small-img3");
                
                SmallImg3[0].onclick = function() 
                {
                    ProductImg3.src = SmallImg3[0].src;
                }
        
                SmallImg3[1].onclick = function() 
                {
                    ProductImg3.src = SmallImg3[1].src;
                }
        
                SmallImg3[2].onclick = function() 
                {
                    ProductImg3.src = SmallImg3[2].src;
                }
                
                SmallImg3[3].onclick = function() 
                {
                    ProductImg3.src = SmallImg3[3].src;
                }
    

            var ProductImg4 = document.getElementById("ProductImg4");
            var SmallImg4 = document.getElementsByClassName("small-img4");
                
                SmallImg4[0].onclick = function() 
                {
                    ProductImg4.src = SmallImg4[0].src;
                }
        
                SmallImg4[1].onclick = function() 
                {
                    ProductImg4.src = SmallImg4[1].src;
                }
        
                SmallImg4[2].onclick = function() 
                {
                    ProductImg4.src = SmallImg4[2].src;
                }
                
                SmallImg4[3].onclick = function() 
                {
                    ProductImg4.src = SmallImg4[3].src;
                }
