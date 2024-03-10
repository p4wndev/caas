document.getElementById("user-input").addEventListener("keydown", (e) => {
	if (e.key === "Enter" && !e.shiftKey) {
		//e.preventDefault();
		sendMessage();
		document.getElementById("user-input").value = "";
	}
});
