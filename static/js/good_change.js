function good_change( url, btnId, goodCountId )
{
    btn = document.querySelector('#'+btnId);
    goodCount = document.querySelector('#'+goodCountId);
    let option = {
        cache: 'no-cache',
       Credential: 'sameorigin'
    };

    fetch(url, option)
    .then( response => response.json())
    .then( data => {
        if( data.status === "OK" )
        {
            if( btn.className == "btn btn-danger")
            {
                btn.className = "btn btn-outline-danger";
            }
            else
            {
                btn.className = "btn btn-danger";
            }
            goodCount.textContent = String(data.good_count);
        }
        else
        {
            alert('いいねに失敗しました');
        }
    })
}