function good_change( url, btnId )
{
    btn = document.querySelector('#'+btnId);
    let option = {
        cache: 'no-cache',
       Credential: 'sameorigin'
    };

    fetch(url, option).then( value => {
        if( btn.className == "btn btn-danger")
        {
            btn.className = "btn btn-outline-danger";
        }
        else
        {
            btn.className = "btn btn-danger";
        }
    })
}