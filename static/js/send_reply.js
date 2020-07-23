let bot = $('#bot_reply');
let msgDiv = $('.display-msgs');
let userInput = $('#userInput');
let chatBox = document.getElementById("box");

userInput.keypress((e) => {
    // Grab the `return` or `enter` keys
    let code = e.keyCode || e.which;
    // If the key `return` or `enter` is pressed
    if (code === 13) {
        let inp = userInput.val();
        let msg = {userMsg: inp};
        

        // append the inputted message to the chat area
        msgDiv.append('<div class="msg_bubble_user">' + inp + '</div>');
        // Auto scroll when messages exceed the height of the box
        chatBox.scrollTop = chatBox.scrollHeight;
        // clear user input
        userInput.val('');

        $.ajax({
            type : 'POST',
            url: '/reply',
            data: JSON.stringify(msg),
            contentType: 'application/json;charset=UTF-8',
            success: (data) => {
            msgDiv.append('<div class="msg_bubble_bot right-align">'+ data.reply +'</div>'); 
            chatBox.scrollTop = chatBox.scrollHeight;
            }
        })
                
    }
});