# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 140 (printed ١٣٩)."""

PAGE_NUMBER = 140
PRINTED_PAGE = "١٣٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "و«مما» يتعلق[[١]] بـ«مختبط»[[٢]]، و«ما» مصدرية[[٣]]، يعني: «ويبكيه أيضا من يسأل بغير وسيلة من أجل إهلاك المهلكات ماله، وما يتوسل به إلى تحصيل المال؛ لأنه كان معطي السائلين بغير وسيلة».",
     "en": "And “mimmā” is attached to “mukhtabiṭ,” and “mā” is maṣdariyya (forming a verbal-noun clause), meaning: “And he is also wept for by one who asks without means, on account of the destroying calamities having ruined his wealth and whatever he uses as a means to acquire wealth — because he [Yazīd] used to give to petitioners without their needing any means.”"},
    {"type": "matn",
     "ar": "٢-(و) قد يحذف الفعل الرافع للفاعل؛ لقيام قرينة دالة على تعيينه[[٤]] (وجوبا) أي: حذفا واجبا (في مثل) قوله تعالى: ﴿وإن أحد من المشركين استجارك﴾[[٥]] أي: في كل موضع حذف الفعل ثم فسر لرفع الإبهام الناشئ من الحذف.",
     "en": "(2) “And” the verb governing the agent may be elided — owing to the presence of an indicator specifying it — “obligatorily,” that is, an obligatory elision, “in the like of” His words, the Exalted: “And if any one of the polytheists seeks your protection” (Qurʾān, Sūrat al-Tawba 9:6) — that is, in every place where the verb is elided and then explicated (mufassar) to remove the ambiguity arising from the elision."},
    {"type": "matn",
     "ar": "فإنه لو ذكر المفسر لم يبق المفسر مفسرا بل صار حشوا، بخلاف المفسر الذي فيه إبهام بدون حذفه، فإنه يجوز الجمع بينه وبين مفسره كقولك: «جاءني رجل أي زيد».",
     "en": "For were the explicated element mentioned, the explicating element would no longer be an explicator but mere padding — unlike an explicated element that contains ambiguity independently of its elision, for there combining it with its explicator is permissible, as in your saying “A man, that is, Zayd, came to me.”"},
    {"type": "matn",
     "ar": "فتقدير الآية: «وإن استجارك أحد من المشركين استجارك»، فـ«أحد» فيها فاعل فعل محذوف وجوبا، وهو «استجارك» الأول المفسر بـ«استجارك» الثاني.",
     "en": "Thus the implied form of the verse is: “And if any one of the polytheists seeks your protection, [he] seeks your protection.” So “aḥad” in it is the agent of an obligatorily elided verb, namely the first “istajāraka,” which is explicated by the second “istajāraka.”"},
    {"type": "matn",
     "ar": "وإنما وجب حذفه؛ لأن مفسره قائم مقامه مغن عنه، ولا يجوز أن يكون «أحد» مرفوعا بالابتداء؛ لامتناع دخول حرف الشرط على الاسم، بل لا بد له من الفعل.",
     "en": "Its elision is obligatory only because its explicator stands in its stead and dispenses with it. It is not permissible for “aḥad” to be nominative as an inchoative (mubtadaʾ), because the conditional particle cannot enter upon a noun; rather, it must have a verb [following it]."},
    {"type": "matn",
     "ar": "٣-(وقد يحذفان) أي: الفعل والفاعل (معا[[٦]]) دون الفاعل وحده (في مثل) «نعم» جوابا (لمن قال: «أقام زيد؟») أي: «نعم، قام زيد» فحذفت الجملة الفعلية[[٧]]، وذكر...",
     "en": "(3) “And the two may be elided” — that is, the verb and the agent — “together,” not the agent alone, “in the like of” “Yes” as an answer “to one who says: Did Zayd stand?” — i.e., “Yes, Zayd stood” — so the verbal sentence is elided; and he mentioned…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ولفظ «مما» متعلق بـ«مختبط» لا بـ«يبكيه»، ففيه تعريض للرضي والهندي.",
     "en": "The expression “mimmā” is attached to “mukhtabiṭ,” not to “yabkīhi”; and in this there is a veiled criticism (taʿrīḍ) of al-Raḍī and al-Hindī."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قال في الحاشية: وتعلقه بـ«يبكيه» المقدر مما يأباه سليقة الشعر؛ لأنه لما بين سبب الضراعة ناسب أن يبين سبب الاختباط أيضا، هذا كلامه.",
     "en": "He said in the gloss: its attachment to the implied “yabkīhi” is something the natural instinct of poetry rejects, because, since he stated the cause of the abasement (ḍarāʿa), it was fitting that he state the cause of the distraction (ikhtibāṭ) as well. These are his words."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأنها أمكن من الموصولة بمعنى «التي أهلكتها الطوائح من الأموال».",
     "en": "Because it (mā maṣdariyya) is more apt than the relative “mā” in the sense of “that of his wealth which the calamities destroyed.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فيه أن القرينة لو كانت دالة على تعيين المحذوف في هذه الصورة لم يلزم الإبهام من حذفه، ولم يحتج إلى ذكر المفسر، بل القرينة في هذه الصورة تدل على أصل الفعل مطلقا لا على تعيينه،",
     "en": "[There is an objection] in it: were the indicator to specify the elided element in this case, no ambiguity would result from its elision, and there would be no need to mention the explicator. Rather, the indicator in this case points to the mere existence of a verb in general, not to its specification;"},
    {"type": "pair",
     "ar": "فإن حرف الشرط في هذا المثال قرينة أصل الفعل لا لخصوص «استجارك» إلا أن يقال: مراده من القرينة الدالة على تعيين المحذوف هي المجموع من حرف الشرط ووجود المفسر، فتأمل.",
     "en": "for the conditional particle in this example is an indicator of a verb’s existence, not of the particular “istajāraka” — unless one says that what he means by “the indicator specifying the elided element” is the totality of the conditional particle together with the presence of the explicator. So ponder it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: فيما حذف وفسر: إما بنفس المحذوف، أو بما يفهم منه معناه، نحو قوله تعالى: ﴿ولو أنهم صبروا﴾ (سورة الحجرات:٥). والتقدير: لو ثبت أنهم صبروا، فحذف «ثبت»، وفسر بأن الثبوت التي خبرها فعل ماض.",
     "en": "That is, in what is elided and then explicated — either by the very [word] elided, or by something from which its meaning is understood — as in His words, the Exalted: “And had they been patient” (Qurʾān, Sūrat al-Ḥujurāt 49:5). The implied form is “had it been established that they were patient,” so “thabata” (was established) is elided and explicated by the affirmation whose predicate is a past-tense verb."},
    {"type": "pair",
     "ar": "وذلك فيما بعد «لو» خاصة سواء كان للشرط أو للتمني. وبهذا ظهر أن ما ذكره الشارح أنه لو ذكر الفعل لصار المفسر حشوا لا يتم.",
     "en": "That obtains specifically in what comes after “law,” whether it be conditional or optative. By this it becomes clear that what the commentator mentioned — that were the verb mentioned, the explicated element would become mere padding — does not hold."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا اختصاص لهذا الحذف بالفعل والفاعل، بل يحذف أي كلام كان سواء كان اسميا أو فعليا، قصيرا كان أو طويلا، مركبا من الفعل والفاعل، أو من الفعل وجميع متعلقاته.",
     "en": "This elision is not restricted to the verb and the agent; rather, any utterance whatsoever may be elided, whether nominal or verbal, short or long, composed of verb and agent, or of the verb together with all its dependents."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "إنما تقدر الجملة؛ لأنا نفهم نسبة تامة. و«نعم» غير صالحة لإفادتها؛ لأنها حرف غير مستقل بالمفهومية.",
     "en": "The sentence is [what is] supplied only because we understand from it a complete predication; and “yes” is not fit to convey it, since it is a particle not independently meaningful."},
]
