from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb
from app.database.request import get_product

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Welcome!')
    
@router.message(F.text == 'Catalog')
async def catalog(message: Message):
    await message.answer('Choose item from Catalog', reply_markup=await kb.categories())
    
@router.callback_query(F.data.startswith('category_'))
async def category_selected(callback: CallbackQuery):
    category_id = callback.data.split('_')[1]
    await callback.message.answer(f'Products by selected category:', reply_markup=await kb.products(category_id))
    await callback.answer('Choosed!')
    
@router.callback_query(F.data.startswith('product_'))
async def product_selected(callback: CallbackQuery):
    product_id = callback.data.split('_')[1]
    product = await get_product(product_id=product_id)
    await callback.message.answer(f'Your product: {product.name}\n{product.description}\nprice: {product.price}€')
    await callback.answer(f'You choosed: {product.name}')
    
