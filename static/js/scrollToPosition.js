//back-to-top button 
const toppestElement = document.querySelector(".toppest-element");
const goToTop = () => {
    toppestElement.scrollIntoView({behavior: "smooth", block: "start", inline: "start"});
};


//back-to-top button 
const about = document.querySelector("#about");
const goToAbout = () => {
    about.scrollIntoView({behavior: "smooth", block: "start", inline: "start"});
    closeMenu();
};


//back-to-top button 
const gallery = document.querySelector("#gallery");
const goToGallery = () => {
    gallery.scrollIntoView({behavior: "smooth", block: "start", inline: "start"});
    closeMenu();
};


//back-to-top button 
const team = document.querySelector(".team");
const goToTeam = () => {
    team.scrollIntoView({behavior: "smooth", block: "start", inline: "start"});
    closeMenu();
};
