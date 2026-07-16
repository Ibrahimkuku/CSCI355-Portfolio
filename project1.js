
"use strict";

    // DARK AND LIGHT MODE

    // I use this section to switch my website between dark mode
    // and light mode when the theme button is clicked.

const themeToggle = document.querySelector("#themeToggle");
const themeIcon = document.querySelector("#themeIcon");
const themeLabel = document.querySelector("#themeLabel");

// This function changes the website theme and updates the button.
function applyTheme(theme) {
    const isDarkMode = theme === "dark";

    document.body.classList.toggle("dark-mode", isDarkMode);

    // I change the icon depending on the current theme.
    if (isDarkMode) {
        themeIcon.className = "fa-solid fa-sun";
        themeLabel.textContent = "Light";
    } else {
        themeIcon.className = "fa-solid fa-moon";
        themeLabel.textContent = "Dark";
    }
}

// I check which theme is currently active and switch to the other one.
themeToggle.addEventListener("click", function () {
    if (document.body.classList.contains("dark-mode")) {
        applyTheme("light");
    } else {
        applyTheme("dark");
    }
});


/*
    MOBILE NAVIGATION MENU

    I use this section to open and close the navigation menu
    when the website is viewed on a smaller screen.
*/

const menuButton = document.querySelector("#menuButton");
const navLinks = document.querySelector("#navLinks");
const navigationItems = navLinks.querySelectorAll("a");

// This opens or closes the mobile navigation menu.
menuButton.addEventListener("click", function () {
    navLinks.classList.toggle("active");

    const menuIcon = menuButton.querySelector("i");

    // I change the menu icon into an X when the menu is open.
    if (navLinks.classList.contains("active")) {
        menuIcon.className = "fa-solid fa-xmark";
    } else {
        menuIcon.className = "fa-solid fa-bars";
    }
});

// I close the mobile menu after one of the navigation links is clicked.
navigationItems.forEach(function (link) {
    link.addEventListener("click", function () {
        navLinks.classList.remove("active");
        menuButton.querySelector("i").className = "fa-solid fa-bars";
    });
});


/*
    IMAGE CAROUSEL

    I store the paths of my portfolio pictures inside this array.
    I can add more pictures later by adding more file paths.
*/

const portfolioPhotos = [
    "project1icon.jpeg",
    "IMG_3542.jpeg",
    "IMG_0018 2.jpeg"
];

const leftButton = document.querySelector("#leftButton");
const rightButton = document.querySelector("#rightButton");
const carouselImage = document.querySelector("#ibrahimPhoto");
const carouselStatus = document.querySelector("#carouselStatus");

let currentPhotoIndex = 0;

// This function displays the picture that matches the current array position.
function showPhoto() {
    carouselImage.src = portfolioPhotos[currentPhotoIndex];

    // This displays which picture the visitor is currently viewing.
    carouselStatus.textContent =
        "Photo " +
        (currentPhotoIndex + 1) +
        " of " +
        portfolioPhotos.length;
}

// This moves the carousel to the previous picture.
leftButton.addEventListener("click", function () {
    currentPhotoIndex--;

    // If I go past the first picture, I return to the last picture.
    if (currentPhotoIndex < 0) {
        currentPhotoIndex = portfolioPhotos.length - 1;
    }

    showPhoto();
});

// This moves the carousel to the next picture.
rightButton.addEventListener("click", function () {
    currentPhotoIndex++;

    // If I go past the last picture, I return to the first picture.
    if (currentPhotoIndex >= portfolioPhotos.length) {
        currentPhotoIndex = 0;
    }

    showPhoto();
});
