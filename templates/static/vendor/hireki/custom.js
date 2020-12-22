// Popover toggler
$('.emoji').popover({
    content:"Copiado xD",
    placement:"top",
    }).click(function (
        ){
        setTimeout(function () {
            $('.emoji').popover('hide');
        }, 1000);
});

// ClipboardJs toggler
new ClipboardJS('.emoji');    
