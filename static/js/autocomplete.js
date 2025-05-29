let availableKeywords = [
    //lantai 0
    'H&M Lantai G',
    'Sociolla',
    'Djournal Coffee Bar',
    'Starbucks Reserve',
    'Marks & Spencer',
    'Pandora',
    'Frank&Co',
    'Tumi',
    'Pintu Keluar 10',
    'Elemis',
    'Miss Mondial',
    "Ling's Sister Jewellery",
    'Melissa Clube',
    'Adelle Jewellery',
    'Timberland',
    'Hyundai',
    'Elevatione',
    'Max Fashion',
    'The Gourmet',
    'Pintu Keluar 9',
    'Axel Vinesse',
    'Kopi Kenangan',
    'Pintu Keluar X',
    'Venchi',
    'Loccitane',
    'Marquine',
    'Toilet Lantai G',

    //lantai 1
    'Uniqlo',
    'Amarissa',
    'Bridges Optical',
    'Cheskee',
    'Colorbox',
    'The Executive',
    'KKV Lantai 1',
    'LockNLock',
    'Miniso',
    'Carla',
    'Parkiran',
    'Urban & Co',
    'Koi The',
    'Dr. Specs',
    'Stop N Go',
    "Levi's",
    'Watch Club',
    'Polo',
    'Glam On',
    'Fossil',
    'Optik Seis Signature',
    'Owl Optical',
    'Zeiss Vision Center',
    'H&M Lantai 1',
    'Toilet Lantai 1',

    //lantai 2
    "Home & Living",
    "Malinda Furniture Gallery",
    "Vivere",
    "Idemu",
    "Payless Shoes",
    "Padre",
    "Iuiga",
    "Urban Republic",
    "Vans",
    "Asics",
    "The Athlete's Foot",
    'Puma',
    'New Era',
    'The North Face',
    'Hoops',
    'Seek',
    'KKV Lantai 2',
    'Lao Fook',
    'Pan & Co',
    'Planet Sports Asia',
    'Converse',
    'Crocs',
    "Tucano's",
    'Adidas',
    'Wee Nam Kee',
    'Fila',
    'Toilet Lantai 2',

    //lantai 3
    'Jiggle Jungle',
    'Reformed Exodus Community',
    'Magal Korean BBQ',
    'Saga Japanese Restaurant',
    'LinCafe',
    'BonCafe',
    'Natural Farm',
    'Shinjuku',
    'Mi Store',
    'Guardian Plus',
    'Vlife Medical',
    'Huawei',
    'Oppo',
    'House of David',
    'Scoop Ideas',
    'Maison Feerie',
    'Pure Clinic',
    'Puro Clinic',
    'Justice',
    'Samsung',
    'Willio',
    'GingerSnaps',
    'Mothercare',
    'Watsons GM3',
    'Nona Manis',
    'Toilet Lantai 3',

    //lantai 4
    'Timezone GM3',
    'ATM BCA GM3',
    'Bakmi GM',
    'Fusia',
    'Ichiban Sushi',
    'Steak 21',
    'Food Court',
    'Poke Theory',
    'Burger King',
    'Crunchaus',
    'Jack & John',
    'Shaburi & Kintan',
    'International Christian Assembly',
    'Toilet Lantai 4'
];

const resultsBox1 = document.getElementById("result-box-1");
const resultsBox2 = document.getElementById("result-box-2");
const pathBox = document.querySelector(".path-box");
const choiceBox = document.querySelector(".choice-box");
const input1 = document.getElementById("user-data-1");
const input2 = document.getElementById("user-data-2");

// Hide result boxes when clicking outside
document.body.addEventListener("click", function(event) {
    if (!resultsBox1.contains(event.target) && !input1.contains(event.target)) {
        resultsBox1.style.display = 'none';
    }
    if (!resultsBox2.contains(event.target) && !input2.contains(event.target)) {
        resultsBox2.style.display = 'none';
    }
});

// Input 1 autocomplete
input1.onkeyup = function(){
    pathBox.innerHTML = '';
    choiceBox.innerHTML = '';
    const routeSummary = document.getElementById("route-summary");
    if (routeSummary) routeSummary.innerHTML = '';

    let result = [];
    let input = input1.value;
    
    if (input.length){
        result = availableKeywords.filter((keyword) => {
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
        console.log("Input 1 results:", result);
    }
    
    display1(result);

    if (!result.length){
        resultsBox1.style.display = 'none';
    }
}

function display1(result){
    if (result.length === 0) {
        resultsBox1.style.display = 'none';
        return;
    }

    const content = result.map((list) => {
        return "<li onclick='selectInput1(this)'>" + list + "</li>";
    });

    resultsBox1.innerHTML = "<ul>" + content.join('') + "</ul>";
    resultsBox1.style.display = 'block';
}

function selectInput1(list){
    const parser = new DOMParser();
    const decodedText = parser.parseFromString(list.innerHTML, 'text/html').body.textContent;
    console.log("Selected input 1:", decodedText);

    input1.value = decodedText;
    resultsBox1.style.display = 'none';
}

// Input 2 autocomplete  
input2.onkeyup = function(){
    pathBox.innerHTML = '';
    choiceBox.innerHTML = '';
    const routeSummary = document.getElementById("route-summary");
    if (routeSummary) routeSummary.innerHTML = '';

    let result = [];
    let input = input2.value;
    
    if (input.length){
        result = availableKeywords.filter((keyword) => {
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
        console.log("Input 2 results:", result);
    }
    
    display2(result);

    if (!result.length){
        resultsBox2.style.display = 'none';
    }
}

function display2(result){
    if (result.length === 0) {
        resultsBox2.style.display = 'none';
        return;
    }

    const content = result.map((list) => {
        return "<li onclick='selectInput2(this)'>" + list + "</li>";
    });

    resultsBox2.innerHTML = "<ul>" + content.join('') + "</ul>";
    resultsBox2.style.display = 'block';
}

function selectInput2(list){
    const parser = new DOMParser();
    const decodedText = parser.parseFromString(list.innerHTML, 'text/html').body.textContent;
    console.log("Selected input 2:", decodedText);

    input2.value = decodedText;
    resultsBox2.style.display = 'none';
}

// Prevent result boxes from closing when clicked
resultsBox1.addEventListener("click", function(event) {
    event.stopPropagation();
});

resultsBox2.addEventListener("click", function(event) {
    event.stopPropagation();
});