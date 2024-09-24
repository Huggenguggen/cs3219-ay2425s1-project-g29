# Nuxt 3 Minimal Starter

Look at the [Nuxt 3 documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

## Setup

Make sure to install the dependencies:

```bash
# npm
npm install
```

## Env Variables
- Set up environment varaibles in a `.env` file
  - `FIREBASE_API_KEY` which you can get from the firebase console.


## Development Server

Start the development server on `http://localhost:3000`:

## Production Build
1. Make sure you are in `Peerprep` directory.
2. Run `docker build -t peerprep .`
3. Run `docker run --rm -it -p 3000:3000 --env-file .env --name peerprep peerprep`

```bash
# npm
npm run dev -- -o
```