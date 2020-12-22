// Popover toggler
$('.btn').popover({
    content:"Copy ;)",
    placement:"top",
    }).click(function (
        ){
        setTimeout(function () {
            $('.btn').popover('hide');
        }, 1000);
});

// ClipboardJs toggler
new ClipboardJS('.btn');    
