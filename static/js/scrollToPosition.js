//back-to-top button 
const toppestElement = document.querySelector(".toppest-element");
const goToTop = () => {
    toppestElement.scrollIntoView({behavior: "smooth", block: "start", inline: "start"});
};


//go to about section code
const about = document.querySelector("#about");
const goToAbout = () => {
    about.scrollIntoView({behavior: "smooth", block: "start", inline: "start"});
    closeMenu();
};


//go to gallery section code 
const gallery = document.querySelector("#gallery");
const goToGallery = () => {
    gallery.scrollIntoView({behavior: "smooth", block: "start", inline: "start"});
    closeMenu();
};


//go to teams section code
const team = document.querySelector(".team");
const goToTeam = () => {
    team.scrollIntoView({behavior: "smooth", block: "start", inline: "start"});
    closeMenu();
};


//go to events section code
const events = document.querySelector("#events");
const goToEvents = () => {
    events.scrollIntoView({behavior: "smooth", block: "start", inline: "start"});
    closeMenu();
};


//go to game section code
const game = document.querySelector("#game");
const goToGame = () => {
    game.scrollIntoView({behavior: "smooth", block: "start", inline: "start"});
    closeMenu();
};
