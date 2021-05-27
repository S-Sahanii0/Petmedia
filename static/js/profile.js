$ = document.querySelector.bind(document);
const b = $("body");
const a = $(".controls__forward a");
const i = $(".controls__forward a i");
const s = $(".controls__forward a span");
const img = $("img");
const m = $("main");

[a, img].forEach((item) => {
    item.addEventListener("click", function (e) {
        e.preventDefault();
        if (img.style.filter === "hue-rotate(-0.45turn)") {
            img.style.filter = "hue-rotate(0)";
        } else {
            img.style.filter = "hue-rotate(-0.45turn)";
        }
        if (b.classList.contains("inverted")) {
            b.classList.remove("inverted");
        } else {
            b.classList.add("inverted");
        }
        if (m.classList.contains("visible")) {
            m.classList.remove("visible");
            s.innerHTML = "More";
            i.classList.replace("fa-times", "fa-bars");
        } else {
            m.classList.add("visible");
            s.innerHTML = "Less";
            i.classList.replace("fa-bars", "fa-times");
        }
    });
});
