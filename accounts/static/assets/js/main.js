// الحصول على العناصر من الصفحة
const navMenu = document.getElementById('nav-menu');
const navToggle = document.getElementById('nav-toggle');

/*===== TOGGLE MENU =====*/
if (navToggle) {
    navToggle.addEventListener('click', () => {
        // تبديل حالة إظهار القائمة
        navMenu.classList.toggle('show-menu');
    });
}

/*===== REMOVE MENU WHEN CLICKING A LINK =====*/
const navLink = document.querySelectorAll('.nav__link');
navLink.forEach(link => {
    link.addEventListener('click', () => {
        // إزالة الكلاس show-menu عند النقر على أي رابط داخل القائمة
        navMenu.classList.remove('show-menu');
    });
});

/*=============== CHANGE BACKGROUND HEADER ===============*/
const scrollHeader = () => {
    const header = document.getElementById('header')
        // When the scroll is greater than 50 viewport height, add the scroll-header class to the header tag
    this.scrollY >= 50 ? header.classList.add('scroll-header') :
        header.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)




/*=============== REMOVE MENU MOBILE ===============*/


const swipeHome2 = new Swiper('.home__swiper', {
    loop: true,
    spaceBetween: 32,
    grabCursor: true,
    effect: 'creative',
    creativeEffect: {
        prev: {
            translate: [-100, 0, -500],
            rotate: [0, 0, 15],
            opacity: 0
        },
        next: {
            translate: [100, 0, -500],
            rotate: [0, 0, -15],
            opacity: 0
        },
    },
    // Autoplay configuration
    autoplay: {
        delay: 3000, // 5 seconds
    },
    // If we need pagination
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
});



var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    grabCursor: true,
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});
/*=============== SHOW SCROLL UP ===============*/
const scrollUp = () => {
    const scrollUp = document.getElementById('scroll-up')
        // When the scroll is higher than 350 viewport height, add the show-scroll class to the a tag with the scrollup class
    this.scrollY >= 350 ? scrollUp.classList.add('show-scroll') :
        scrollUp.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollUp)
const swiper1 = new Swiper('#swiper1', {
    loop: true,
    spaceBetween: 16,
    slidesPerView: 'auto',
    autoplay: {
        delay: 3000, // الوقت بالمللي ثانية (3000 مللي ثانية = 3 ثوانٍ)
        disableOnInteraction: false,
    },
    breakpoints: {
        1150: {
            slidesPerView: 3,
        },
    }
});

const swiper2 = new Swiper('#swiper2', {
    loop: true,
    spaceBetween: 16,
    slidesPerView: 'auto',
    autoplay: {
        delay: 3000, // الوقت بالمللي ثانية (3000 مللي ثانية = 3 ثوانٍ)
        disableOnInteraction: false,
        reverseDirection: true, // لتحريك الشريط إلى اليسار
    },
    breakpoints: {
        1150: {
            slidesPerView: 3,
        },
    }
});
/*=============== SHOW & HIDE MENU ===============*/
const toggleButton = document.getElementById('floating-toggle');

const toggleMenu = () => {
    toggleButton.classList.toggle('active');
};

toggleButton.addEventListener('click', toggleMenu);

document.getElementById('scroll-up').addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});