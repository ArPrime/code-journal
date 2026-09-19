# 🚀 把 Claude Artifact 部署到 Vercel —— 纯小白教程

## 你需要准备什么

- 一个 GitHub 账号（免费注册：https://github.com）
- 一个 Vercel 账号（免费注册：https://vercel.com，可以用 GitHub 直接登录）
- 你的 Claude Artifact 的 TSX 代码

---

## 第一步：下载这个项目

把这个文件夹下载到你的电脑上。

---

## 第二步：把你的 Artifact 代码放进去

1. 用任意文本编辑器（推荐 VS Code，免费下载：https://code.visualstudio.com）打开 `src/App.tsx`
2. **删除** `src/App.tsx` 里的全部内容
3. **粘贴**你的 Claude Artifact 代码
4. **关键一步**：确保文件末尾有 `export default 你的组件名`

### 举个例子

假设你的 artifact 代码长这样：

```tsx
import { useState } from "react"

const TodoApp = () => {
  const [todos, setTodos] = useState([])
  return <div>...</div>
}
```

你需要在最后加一行：

```tsx
export default TodoApp
```

如果你的 artifact 代码已经有 `export default`，就不用加了。

### 如果代码用了 shadcn/ui 组件怎么办？

Claude artifact 里 `import { Button } from '@/components/ui/button'` 这类 shadcn 导入在独立项目里不能直接用。最简单的办法是把 shadcn 组件替换成普通 HTML + Tailwind：

- `<Button>` → `<button className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">`
- `<Card>` → `<div className="border rounded-lg p-4 shadow">`
- `<Input>` → `<input className="border rounded px-3 py-2 w-full">`

---

## 第三步：上传到 GitHub

### 方式 A：用 GitHub 网页（最简单）

1. 登录 https://github.com
2. 点右上角 **"+"** → **"New repository"**
3. 给仓库取个名字（比如 `my-app`），点 **"Create repository"**
4. 在新仓库页面点 **"uploading an existing file"**
5. 把这个项目文件夹里的**所有文件**拖进去（不要拖文件夹本身，要拖里面的内容）
6. 点 **"Commit changes"**

### 方式 B：用命令行（如果你装了 Git）

```bash
cd deploy-artifact-to-vercel
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/你的用户名/你的仓库名.git
git push -u origin main
```

---

## 第四步：在 Vercel 部署

1. 打开 https://vercel.com 并登录（推荐用 GitHub 账号登录）
2. 点 **"Add New..."** → **"Project"**
3. 找到你刚创建的 GitHub 仓库，点 **"Import"**
4. Vercel 会自动检测到这是一个 Vite 项目，默认设置不用改
5. 点 **"Deploy"**
6. 等 1-2 分钟，部署完成！
7. Vercel 会给你一个 `xxx.vercel.app` 的网址，点开就能看到你的应用了

---

## 常见问题

### Q: 部署失败了怎么办？

看 Vercel 的构建日志（Build Logs），最常见的错误是：
- **TypeScript 类型错误**：在 `tsconfig.json` 里已经关掉了严格的 unused 检查
- **缺少依赖**：如果你的 artifact 用了特殊的库，需要在 `package.json` 的 `dependencies` 里加上

### Q: 怎么更新网站？

只要你更新 GitHub 仓库里的代码，Vercel 会自动重新部署。

### Q: 能绑定自己的域名吗？

可以！在 Vercel 项目的 **Settings** → **Domains** 里添加你的域名。

---

## 项目结构说明

```
deploy-artifact-to-vercel/
├── index.html          ← 网页入口
├── package.json        ← 项目依赖配置
├── vite.config.ts      ← Vite 构建工具配置
├── tsconfig.json       ← TypeScript 配置
├── tailwind.config.js  ← Tailwind CSS 配置
├── postcss.config.js   ← PostCSS 配置
└── src/
    ├── main.tsx        ← 应用入口（不用改）
    ├── index.css       ← 全局样式（不用改）
    └── App.tsx         ← ⭐ 把你的 artifact 代码放这里
```

你只需要改 `src/App.tsx` 这一个文件就行了！
