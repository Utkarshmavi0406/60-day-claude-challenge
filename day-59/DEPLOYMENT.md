# RiskLens — Deploying to Render.com (Free Tier)

Follow these steps exactly. Render deploys directly from your GitHub repo, so make sure everything from today is committed and pushed to risklens before starting.

## Step 1 — Create a Render account

1. Go to render.com
2. Click Get Started
3. Sign up using GitHub (this makes connecting your repo in Step 2 automatic)
4. Authorize Render to access your GitHub account when prompted

## Step 2 — Create the Web Service

1. From the Render Dashboard, click New + (top right)
2. Select Web Service
3. Under "Connect a repository," find and select risklens (if it's not listed, click Configure account and grant Render access to that repo specifically)
4. Click Connect next to risklens

## Step 3 — Configure the service

Fill in these exact fields:

| Field | Value |
|---|---|
| Name | risklens (or any name, this becomes part of your URL) |
| Region | Closest to you |
| Branch | main |
| Root Directory | leave blank |
| Runtime | Python 3 |
| Build Command | pip install -r requirements.txt |
| Start Command | uvicorn api.main:app --host 0.0.0.0 --port $PORT |
| Instance Type | Free |

## Step 4 — Deploy

1. Scroll down and click Create Web Service
2. Render will start building automatically, watch the build logs on screen
3. This takes a few minutes the first time. Watch for:
   - "Model and SHAP explainer loaded successfully at startup." - confirms your model loaded correctly
   - "Uvicorn running on http://0.0.0.0:$PORT" - confirms the server started
4. Once the status at the top changes to Live, your app is running publicly

## Step 5 — Get your live URL

Your URL appears at the top of the Render dashboard page, in the format:
https://risklens-xxxx.onrender.com

Click it to open your live app.

## Step 6 — Verify it actually works

1. The RiskLens form should load
2. Click one of the sample applicant buttons (e.g. "High Risk")
3. Click Predict Risk
4. Confirm you get back a real probability, risk tier, and factor list

Known free-tier behavior: if the app has been inactive for a while, the first request after inactivity can take 30-60 seconds while Render spins the service back up, this is normal free-tier cold-start behavior, not a bug. Subsequent requests will be fast.

## Step 7 — Confirm and share

Take a screenshot of the live app working, and share the live URL, that's the link that goes in your README, your resume, and your LinkedIn post.

## If the build fails

Check the build logs for the specific error. Common causes:
- A missing package in requirements.txt, everything needed should already be there from today's session
- If you see a memory error during build (rare on free tier with this stack), let me know and we can look at trimming dependencies
