import { redirect } from '@sveltejs/kit';
export async function handle({ event, resolve }) {

    if (event.url.pathname === '/calendar') {
        throw redirect(303, '/login');
    }

    const response = await resolve(event);
    return response;
}