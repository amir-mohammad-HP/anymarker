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
        // $('html, body').animate({scrollTop: 0}, 1700, 'easeInOutExpo');
        $('html, body').scrollTop(1)
        return false;
    });


    // Sidebar Toggler
    $('.sidebar-toggler').click(function () {
        $('.sidebar, .content').toggleClass("open");
        return false;
    });
    
    const hostName = window.location.origin;
    
    // CONTROL CONTENT :
        // get collections information 

            // - apply collections information

            $.ajax({
                url : hostName + "/api/collection/?format=json",
                dataType: "json",
                success : function (data) {
                        $("#slider").empty()
                        
                        function collection_handler(collection_data){

                            let sliderItem = `
                                <div class="nav-item dropdown">
                                    <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown"><i class="fa fa-th me-2"></i>`+ collection_data.name +`</a>
                                    <div class="dropdown-menu bg-transparent border-0" id="collection-`+ collection_data.id +`">
                                        <!-- link to marks
                                            <a href="button.html" class="dropdown-item">Buttons</a> 
                                        -->
                                    </div>
                                </div>
                            `;
                            $("#slider").prepend(sliderItem);
                        };
                        data.forEach(element => {
                            collection_handler(element)
                        });
                        let button_add_collection = '<a href="index.html" class="nav-item nav-link"><i class="fa fa-tachometer-alt me-2"></i>add collection</a>'
                        $("#slider").prepend(button_add_collection)
                    }
                    });
            $("#Content_main").empty()
            // this is the first view user will see
            $("#Content_main").html(ContentProfileView) // the ContentProfileView has defined in the collection.html, 

        // get marks 
            $.ajax({
                url : hostName + "/api/mark/?format=json",
                dataType: "json",
                success : function (data) {

                        mark_data = data;

                        function collection_id_handler(mark){
                            
                            let Item_html = `
                                <a class="dropdown-item" id="mark-`+ mark.id +`">`+ mark.name +`</a> 
                            `;

                            $("#collection-"+ mark.collection).prepend(Item_html);

                            let mark_id = "#mark-" + mark.id ;

                            $(mark_id).css('cursor', 'pointer'); // fix css cursor on element
                            
                            // add onclick event listenner
                            $(mark_id).on('click', function(){
                                
                                $('#Content_main').empty()
                                toggleContentSpinner();
                               
                                // get the information of the selected mark
                                let mark_relevant_detail_url;
                                if (mark.model == 'url'){

                                    mark_relevant_detail_url = hostName + "/api/urls/" + mark.id + "/?format=json";

                                } else if (mark.model == 'image'){

                                    mark_relevant_detail_url = hostName + "/api/images/" + mark.id + "/?format=json";

                                } else if (mark.model == 'note'){

                                    mark_relevant_detail_url = hostName + "/api/notes/" + mark.id + "/?format=json";
                                };
                                built_note_view(mark_relevant_detail_url, mark);
                                untoggleContentSpinner();
                                    
                            })
                        };
                        data.forEach(element => {
                            collection_id_handler(element)
                        });
                    }
                    });
        
        // mark controls functions :
        // get notifications

            // - apply notifications

})

const toggleContentSpinner = () => {
    if ($('#content-spinner').length) {

    }else{
        let spin_content = `
            <div id="content-spinner" class="show bg-dark position-relative translate-end w-100 vh-100 top-50 start-0 d-flex align-items-center justify-content-center">
                <div class="spinner-border text-primary" style="width: 3rem; height: 3rem;" role="status">
                    <span class="sr-only">Loading...</span>
                </div>
            </div>
        `;

        $('#Content_main').empty();
        $('#Content_main').prepend(spin_content);

    }
}

const untoggleContentSpinner = () => {
    if ($('#content-spinner').length) {

        $('#content-spinner').remove();
        
};
}

const built_note_view = (url, markData) => {
    $.ajax({
        url : url,
        dataType:"json",
        success : function (data){
            built_view(data, url, markData)
        },
        error: function () {
            
            $('#Content_main').empty();
            $('#Content_main').prepend(`
            <div id="404" class="position-relative translate-end w-100 vh-100 top-50 start-0 d-flex align-items-center justify-content-center">
                the request wasn't success , information not found
            </div>
            `);
        },
    })
}

const built_view = (data, url, markData) => {
    if (data.detail === 'Not found.'){
        $('#Content_main').empty();
        $('#Content_main').prepend(`
        <div id="404" class="position-relative translate-end w-100 vh-100 top-50 start-0 d-flex align-items-center justify-content-center">
               the request wasn't success , information not found , must maintain the partition to create parts
        </div>
        `);

    }else{

        let view = '<p> found </p>';
        $('#Content_main').empty();
        $('#Content_main').prepend(data.template);
        console.log(markData);
        console.log(url);
    }
}

