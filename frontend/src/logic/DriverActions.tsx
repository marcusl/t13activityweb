import { Driver } from "../Models";
import { getJsonHeaders } from './ADRActions';

const fixDriverDate = (key:string, value:any) => {
    if (key === 'birthday') {
        return value.split('T')[0]; // remove time part        
    }

    return value;
}

export const deleteDriverAsync  = async (driver: Driver) => {
    const r = await fetch(driver.apiUrl(), {
        method: 'DELETE',
        headers: getJsonHeaders(),
        body: JSON.stringify(driver)
    });

    if (r.status >= 300) {
        console.error(r.status + ': ' + r.statusText);
        throw (await r.text())
    }
}

export const updateDriverAsync = async (driver: Driver) => {
    const r = await fetch(driver.apiUrl(), {
        method: 'PATCH',
        headers: getJsonHeaders(),
        body: JSON.stringify(driver, fixDriverDate)
    });

    if (r.status >= 300) {
        console.error(r.status + ': ' + r.statusText);
        throw (await r.text())
    }
}

// throws on error
export const createDriverAsync = async (driver: Driver) => {
    const r = await fetch(Driver.apiUrlForId(''), {
        method: 'PUT',
        headers: getJsonHeaders(),
        body: JSON.stringify(driver, fixDriverDate)
    });

    if (r.status >= 300) {
        console.error(r.status + " " + r.statusText)
        throw (await r.text())
    }

    const data = await r.json();
    driver.id = data.id;
    return driver;
}

