const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () = > {
        container.classList.add("right-panel-active"),
con = document.getElementById("container")
con.style = "width:1300px;transition: all 0.6s ease-in-out"
})
;

signInButton.addEventListener('click', () = > {
    container.classList.remove("right-panel-active");
document.getElementById("container").style.width = "750px"
})
;
