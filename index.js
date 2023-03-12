import { getElement, getElements, Collapsible, getTemplate, hasOwn, htmlToElement } from 'zenkai'
// import './assets/css/normalize.css';
// import './assets/css/base.css';
// import './assets/css/style.css';

import TEACHERS_DATA from './data/teachers.yml';
// import WEEK_DATA from './data/weeks.yml';


let body = getElement('.body-content');

let teachers = getElement(`[data-name="teachers"]`);

let schedule = getElements(`[data-name="schedule"]`);

let weeks = getElement(`[data-name="weeks"]`);

if (teachers) {
    let tplTeacher = getTemplate("#tpl-teacher");
    let content = tplTeacher.innerHTML;

    TEACHERS_DATA.forEach(teacher => {
        let tplElement = htmlToElement(parse(content, teacher));
        teachers.append(tplElement);
    });
}

if (weeks) {
    let tplWeek = getTemplate("#tpl-week");
    let content = tplWeek.innerHTML;

    WEEK_DATA.forEach(data => {
        let tplElement = htmlToElement(parse(content, data));

        bindContent(tplElement, data);

        weeks.append(tplElement);
    });
}

Collapsible(body);

function bindContent(element, data) {
    let children = getElements(`[data-item]`, element);

    children.forEach(child => {
        const { item, bind } = child.dataset;

        let bindData = data[bind];
        let template = getTemplate(`#${item}`);
        let content = template.innerHTML;

        bindData.forEach(bd => {
            let parsedElement = htmlToElement(parse(content, bd))

            let subitems = getElements(`[data-item]`, parsedElement);
            if (subitems) {
                bindContent(parsedElement, bd);
            }

            child.append(parsedElement);
        })
    });
}

function parse(content, data) {
    var result = content.trim();

    let matches_value = result.match(/(\$value)/g)
    if (matches_value) {
        matches_value.forEach((key, i) => {
            result = result.replace(key, data);
        });
    }

    let matches = result.match(/(#[A-Za-z0-9_]+)/g)
    if (matches) {
        matches.forEach((key, i) => {
            let attr = key.substring(1);
            if (hasOwn(data, attr)) {
                result = result.replace(key, data[attr]);
            }
        });
    }

    return result;
}
