document.getElementById("user-input").addEventListener("keydown", (e) => {
	if (e.key === "Enter" && !e.shiftKey) {
		//e.preventDefault();
		sendMessage();
		document.getElementById("user-input").value = "";
	}
});

document.getElementById("btn-dhct").onclick = () => {
	setSchool("Trường Đại Học Cần Thơ");
};
document.getElementById("btn-cntt").onclick = () => {
	setSchool("Trường Công nghệ Thông tin & Truyền Thông - ĐHCT");
};
document.getElementById("btn-kt").onclick = () => {
	setSchool("Trường Kinh tế - ĐHCT");
};

function setSchool(school) {
	console.log("hello");
	document.getElementById("selected-school").innerText = school;
}
