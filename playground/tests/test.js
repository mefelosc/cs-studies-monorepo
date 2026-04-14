
let emotionRadios = document.getElementById('emotion-radios')


function renderEmotionsRadios(cats){
    const emotions = getEmotionsArray(cats)
    let radioItems = ''
    emotions.forEach(emotion => {
        radioItems += `
        <p>
            <input 
                type="radio" 
                id="${emotion}" 
                name="emotions" 
                value="${emotion}"
            >
            <label for="${emotion}">${emotion}</label>
        </p>
        `
    })
    emotionRadios.innerHTML = radioItems
}

renderEmotionsRadios(catsData)