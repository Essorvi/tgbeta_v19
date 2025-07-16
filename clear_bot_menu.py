#!/usr/bin/env python3
"""
Скрипт для очистки меню команд бота
"""

import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv('backend/.env')

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

def clear_bot_menu():
    """Очищает меню команд бота"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/setMyCommands"
    
    # Отправляем пустой список команд
    payload = {
        "commands": []
    }
    
    try:
        response = requests.post(url, json=payload)
        result = response.json()
        
        if result.get('ok'):
            print("✅ Меню команд бота успешно очищено!")
            print("🔄 Перезапустите бота для применения изменений")
        else:
            print(f"❌ Ошибка: {result.get('description', 'Неизвестная ошибка')}")
            
    except Exception as e:
        print(f"❌ Ошибка при очистке меню: {e}")

def get_current_commands():
    """Получает текущие команды бота"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getMyCommands"
    
    try:
        response = requests.get(url)
        result = response.json()
        
        if result.get('ok'):
            commands = result.get('result', [])
            if commands:
                print("📋 Текущие команды бота:")
                for cmd in commands:
                    print(f"  /{cmd['command']} - {cmd['description']}")
            else:
                print("📋 У бота нет команд в меню")
        else:
            print(f"❌ Ошибка получения команд: {result.get('description')}")
            
    except Exception as e:
        print(f"❌ Ошибка при получении команд: {e}")

if __name__ == "__main__":
    print("🤖 Скрипт очистки меню бота")
    print("=" * 40)
    
    if not TELEGRAM_TOKEN:
        print("❌ Токен бота не найден в .env файле")
        exit(1)
    
    print("🔍 Проверяем текущие команды...")
    get_current_commands()
    
    print("\n🗑️ Очищаем меню команд...")
    clear_bot_menu()
    
    print("\n✅ Готово! Старые кнопки меню должны исчезнуть.")