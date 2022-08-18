$(document).ready(function () {
    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Sidebar Toggler
    $('.sidebar-toggler').click(function () {
        $('.sidebar, .content').toggleClass("open");
        return false;
    });
    
    
    // CONTROL CONTENT :
        // get collections information 

            // - apply collections information

            $.ajax({
                url : "http://127.0.0.1:8000/api/collection/?format=json",
                dataType: "json",
                success : function (data) {
                        $("#slider").empty()
                        
                        function collection_handler(collection_data){
                            
                            // get marks information

                            let sliderItem = `
                                <div class="nav-item dropdown">
                                    <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown"><i class="fa fa-th me-2"></i>`+ collection_data.name +`</a>
                                    <div class="dropdown-menu bg-transparent border-0">
                                        <a href="button.html" class="dropdown-item">Buttons</a> 
                                        <a href="typography.html" class="dropdown-item">Typography</a>
                                        <a href="element.html" class="dropdown-item">Other Elements</a>
                                    </div>
                                </div>
                            `;
                            $("#slider").append(sliderItem);
                        };
                        data.forEach(element => {
                            collection_handler(element)
                        });
                    }
                    });

    
        // get notifications

            // - apply notifications

})



