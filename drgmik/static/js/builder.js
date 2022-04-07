let prgCount = 0;
let imgCount = 0;

let lineIndex = 0;

const prgClass = "w-full ring-1 ring-light-900 bg-dark-900 mt-3 p-3";
const prgRows = "10";
const prgCols = "40";
const prgPlaceholder = "Enter a pragraph here...";

const lineIndexMin = "1";
const lineIndexMax = "20"

function incrementTotalForms(id) {
	const totalForms = document.getElementById(id);
	const value = totalForms.getAttribute("value");
	totalForms.setAttribute("value", parseInt(value) + 1);
}

function addParagraph() {
	const prgId = `id_prg-${prgCount}-text`;
	const prgName = `prg-${prgCount}-text`;
	const prgElement = document.createElement("textarea");

	prgElement.setAttribute("id", prgId);
	prgElement.setAttribute("name", prgName);
	prgElement.setAttribute("cols", prgCols);
	prgElement.setAttribute("rows", prgRows);
	prgElement.setAttribute("class", prgClass);
	prgElement.setAttribute("placeholder", prgPlaceholder);

	const prgIndexId = `id_prg-${prgCount}-index`;
	const prgIndexName = `prg-${prgCount}-index`;
	const index = document.createElement("input");

	index.setAttribute("id", prgIndexId);
	index.setAttribute("type", "hidden");
	index.setAttribute("name", prgIndexName);
	index.setAttribute("value", lineIndex);
	index.setAttribute("min",lineIndexMin);
	index.setAttribute("max", lineIndexMax);


	const createForms = document.getElementById("create-forms");
	createForms.appendChild(prgElement);
	createForms.appendChild(index);

	incrementTotalForms("id_prg-TOTAL_FORMS");

	prgCount++;
	lineIndex++;
}

function addImage() {
	const imgId = `id_img-${imgCount}-img`;
	const imgName = `img-${imgCount}-img`;	
	const imgElement = document.createElement("input");

	imgElement.setAttribute("id", imgId);
	imgElement.setAttribute("type", "file");
	imgElement.setAttribute("name", imgName);
	imgElement.setAttribute("accept", "image/*");

	const imgIndexId = `id_img-${imgCount}-index`;
	const imgIndexName = `img-${imgCount}-index`;
	const index = document.createElement("input");

	index.setAttribute("id", imgIndexId);
	index.setAttribute("type", "hidden");
	index.setAttribute("name", imgIndexName);
	index.setAttribute("value", lineIndex);
	index.setAttribute("min", lineIndexMin);
	index.setAttribute("max", lineIndexMax);

	const createForms = document.getElementById("create-forms");
	createForms.appendChild(imgElement);
	createForms.appendChild(index);

	incrementTotalForms("id_img-TOTAL_FORMS");

	imgCount++;
	lineIndex++;
}