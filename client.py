html = """
&lt;!DOCTYPE html&gt;
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Chat&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;h1&gt;WebSocket Chat&lt;/h1&gt;
        &lt;form action="" onsubmit="sendMessage(event)"&gt;
            &lt;input type="text" id="messageText" autocomplete="off"/&gt;
            &lt;button&gt;Send&lt;/button&gt;
        &lt;/form&gt;
        &lt;ul id='messages'&gt;
        &lt;/ul&gt;
        &lt;script&gt;
            var ws = new WebSocket("ws://localhost:7000");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        &lt;/script&gt;
    &lt;/body&gt;
&lt;/html&gt;
"""