document.addEventListener("DOMContentLoaded", () => {
  const chatWindow = document.getElementById("chat-window");
  const userInput = document.getElementById("user-input");
  const sendButton = document.getElementById("send-button");

  function appendMessage(sender, message) {
    if (!chatWindow) {
      console.error("❌ chat-window element not found");
      return;
    }

    const containerDiv = document.createElement("div");
    containerDiv.className = "message-container " + sender + "-container";

    const avatarImg = document.createElement("img");
    avatarImg.className = "avatar";
    avatarImg.src = sender === "user" ? "/static/user-avatar.png" : "/static/bot-avatar.png"; // ✅ Fixed path!

    const messageDiv = document.createElement("div");
    messageDiv.className = "message " + sender;
    messageDiv.textContent = message;

    containerDiv.appendChild(avatarImg);
    containerDiv.appendChild(messageDiv);

    chatWindow.appendChild(containerDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }

  async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    appendMessage("user", message);
    userInput.value = "";

    try {
      const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });

      const data = await response.json();
      appendMessage("bot", data.response);
    } catch (error) {
      console.error("Error:", error);
      appendMessage("bot", "Something went wrong. Please try again.");
    }
  }

  sendButton.addEventListener("click", sendMessage);

  userInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  });
});
