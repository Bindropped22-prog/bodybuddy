document.addEventListener("DOMContentLoaded", function () {
    const dietSelect = document.querySelector('select[name="diet"]');
    const otherDietContainer = document.getElementById("other-diet-container");

    if (dietSelect) {
        dietSelect.addEventListener("change", function () {
            const selectedOptions = Array.from(dietSelect.selectedOptions);
            const showOther = selectedOptions.some(opt => opt.value === "Other");
            otherDietContainer.style.display = showOther ? "block" : "none";
        });
    }
});
