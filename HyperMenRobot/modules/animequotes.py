import random
import HyPerMenRobot.modules.animequotesstring as animequotesstring

from telegram import Update
from telegram.ext import CallbackContext, run_async
from HyPerMenRobot import dispatcher
from HyPerMenRobot.modules.disable import DisableAbleCommandHandler


@run_async
def animequotes(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(animequotesstring.ANIMEQUOTES))


ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequotes", animequotes)

dispatcher.add_handler(ANIMEQUOTES_HANDLER)
