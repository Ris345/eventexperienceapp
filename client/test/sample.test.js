import { cleanup, render, screen } from '@testing-library/svelte'
import LoginPage from '../src/routes/(app)/login/+page.svelte'

describe('login page.svelte', () => {
    // TODO: @testing-library/svelte claims to add this automatically but it doesn't work without explicit afterEach
    afterEach(() => cleanup())

    it('mounts', () => {
        const { container } = render(LoginPage)
        expect(container).toBeTruthy()
        expect(container.innerHTML).toContain('Login')
    })

    it('has title', () => {
        render(LoginPage)
        // console.log(screen.debug());
        const heading = screen.getByRole('heading', { level: 2 })
        expect(heading).toBeInTheDocument()
    })

    it('has login button', async () => {
        render(LoginPage)
        const btn = screen.getByRole('button')
        expect(btn.textContent.trim()).toBe('Login')
    })
})
