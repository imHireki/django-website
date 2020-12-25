// Popover toggler
$('.copy').popover({
    content:"Copiado xD",
    placement:"top",
    }).click(function (
        ){
        setTimeout(function () {
            $('.copy').popover('hide');
        }, 1000);
});

// ClipboardJs toggler
new ClipboardJS('.copy');    
