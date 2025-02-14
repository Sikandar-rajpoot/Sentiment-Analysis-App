$root = "sentiment-analysis-app"

$dirs = @(
    "$root/backend/app/api/v1/endpoints",
    "$root/backend/app/models",
    "$root/backend/app/schemas",
    "$root/backend/app/services",
    "$root/backend/app/tasks",
    "$root/backend/app/utils",
    "$root/backend/app/core",
    "$root/frontend/src/components",
    "$root/frontend/src/pages",
    "$root/frontend/src/services",
    "$root/frontend/src/utils"
)

$files = @(
    "$root/backend/app/__init__.py",
    "$root/backend/app/api/__init__.py",
    "$root/backend/app/api/v1/__init__.py",
    "$root/backend/app/api/v1/api.py",
    "$root/backend/app/api/v1/endpoints/__init__.py",
    "$root/backend/app/api/v1/endpoints/comments.py",
    "$root/backend/app/api/v1/endpoints/analysis.py",
    "$root/backend/app/models/__init__.py",
    "$root/backend/app/models/comment.py",
    "$root/backend/app/schemas/__init__.py",
    "$root/backend/app/schemas/comment.py",
    "$root/backend/app/services/__init__.py",
    "$root/backend/app/services/sentiment_analysis.py",
    "$root/backend/app/services/database_service.py",
    "$root/backend/app/tasks/__init__.py",
    "$root/backend/app/tasks/celery_app.py",
    "$root/backend/app/tasks/sentiment_tasks.py",
    "$root/backend/app/utils/__init__.py",
    "$root/backend/app/utils/config.py",
    "$root/backend/app/utils/dependencies.py",
    "$root/backend/app/core/__init__.py",
    "$root/backend/app/core/database.py",
    "$root/backend/app/main.py",
    "$root/backend/app/worker.py",
    "$root/backend/.env",
    "$root/backend/requirements.txt",
    "$root/backend/Dockerfile",
    "$root/frontend/src/App.js",
    "$root/frontend/src/index.js",
    "$root/frontend/package.json",
    "$root/frontend/Dockerfile",
    "$root/docker-compose.yml",
    "$root/README.md"
)

# Create directories
foreach ($dir in $dirs) {
    if (!(Test-Path -Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
}

# Create files
foreach ($file in $files) {
    if (!(Test-Path -Path $file)) {
        New-Item -ItemType File -Path $file -Force | Out-Null
    }
}

Write-Host "Project structure created successfully!"
