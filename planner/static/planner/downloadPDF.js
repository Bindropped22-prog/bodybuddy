document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("save-pdf-btn");

    btn.addEventListener("click", function () {
        const content = document.getElementById("plan-content");
        const opt = {
            margin:       0.5,
            filename:     'BodyBuddy_Plan.pdf',
            image:        { type: 'jpeg', quality: 0.98 },
            html2canvas:  { scale: 2 },
            jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
        };

        html2pdf().set(opt).from(content).save();
    });
});
