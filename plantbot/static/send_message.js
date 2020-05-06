
var  i = 1;
$(function() {
   
    function submit_message(message) {
        
        $.post( "/send_message", {message: message}, handle_response);
        
        function handle_response(data) {
            // append the bot repsonse to the div
            console.log(data.message)
            if(data.message =='back'){
                window.location.replace('/');
            }
            $('.chat-box').append(`
                <div class="chat-l">
                    <div class="mess">
                        <p id="div${i}">${data.message}</p>
                    </div>
                    <div class="sp"></div>
                </div> 
            `)
            
            console.log(i);

            // remove the loading indicator
            $( "#loading" ).remove();
            scroll_down()
            i = i+1;
        }
        
    }
    function scroll_down(){
        var elmnt = document.getElementById("div"+i);
        elmnt.scrollIntoView();
        console.log(i);

    }

    $('#target').on('submit', function(e){
        e.preventDefault();
        const input_message = $('#input_message').val()
        // return if the user does not enter any text
        if (!input_message) {
            return
        }

        $('.chat-box').append(`
            <div class="chat-r">
                <div class="sp"></div>
                    <div class="mess mess-r">
                        <p>${input_message}</p>
                    </div>
                </div>
            </div>
        `)
        
        console.log(i);
        // loading
        $('.chat-box').append(`
            <div class="chat-l" id="loading">
                <div class="mess">
                    <p id="div${i}">...</p>
                </div>
                <div class="sp"></div>
            </div>
        `)
        scroll_down()
        // clear the text input
        $('#input_message').val('')

        // send the message
        submit_message(input_message)
    });

});