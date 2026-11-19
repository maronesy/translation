# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 59 (printed ٥٨)."""

PAGE_NUMBER = 59
PRINTED_PAGE = "٥٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "١- فمن خواص الاسم: (دخول اللام) أي: لام التعريف[[١]].",
     "en": "1 — Among the special properties of the noun (ism) is (the entry of the lām), that is, the lām of definiteness (lām al-taʿrīf)."},
    {"type": "matn",
     "ar": "ولو قال[[٢]]: دخول حرف التعريف[[٣]] لكان شاملا للميم في قوله صلى الله عليه وسلم: «ليس من امبر امصيام في امسفر»، لكنه[[٤]] لم يتعرض له[[٥]] لعدم شهرته،",
     "en": "Had he said “the entry of the definite particle (ḥarf al-taʿrīf),” it would have encompassed the mīm [used as the article] in his saying, may Allah bless him and grant him peace: “It is not of piety to fast while travelling” (laysa min am-birri am-ṣiyāmu fī am-safar); but he did not treat of it, on account of its lack of currency,"},
    {"type": "matn",
     "ar": "وفي اختياره[[٦]] اللام إشارة إلى أن المختار عنده ما ذهب إليه سيبويه من أن أداة التعريف هي اللام وحدها[[٧]]، زيدت عليها همزة الوصل، لتعذر الابتداء بالساكن[[٨]].",
     "en": "and in his choosing “the lām” there is an indication that the preferred view in his opinion is that adopted by Sībawayh: that the instrument of definiteness is the lām alone, to which the conjunctive hamza (hamzat al-waṣl) was added because beginning with a quiescent letter is impossible."},
    {"type": "matn",
     "ar": "وأما الخليل: فقد ذهب إلى أنها «ال» كـ«هل»[[٩]] و«بل».",
     "en": "As for al-Khalīl, he held that it is “al,” like “hal” and “bal.”"},
    {"type": "matn",
     "ar": "والمبرد: إلى أنها[[١٠]] الهمزة[[١١]] المفتوحة زيدت اللام، للفرق بينها وبين همزة الاستفهام.",
     "en": "And al-Mubarrad [held] that it is the fatḥa-bearing hamza, to which the lām was added in order to distinguish it from the interrogative hamza (hamzat al-istifhām)."},
    {"type": "matn",
     "ar": "وإنما اختص دخول حرف التعريف بالاسم؛ لأنه[[١٢]] لتعيين معنى مستقل[[١٣]] بالمفهومية، يدل عليه اللفظ مطابقة، والحرف لا يدل على المعنى المستقل بالمفهومية، والفعل يدل عليه تضمنا لا مطابقة.",
     "en": "The entry of the definite particle is restricted to the noun only because it serves to specify a meaning that is independent in its conceivability (mafhūmiyya) — one that the wording (lafẓ) denotes by full correspondence (muṭābaqa); whereas the particle (ḥarf) does not denote a meaning independent in conceivability, and the verb (fiʿl) denotes it by implication (taḍammun) rather than by correspondence."},
    {"type": "matn",
     "ar": "وهذه الخاصة ليست شاملة لجميع أفراد الاسم، فإن حرف التعريف لا يدخل",
     "en": "Yet this property does not encompass every individual instance of the noun, for the definite particle does not enter"},

    {"type": "rule"},

    # ---------------- Footnotes ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "احترز به عن لام الأمر ولام الابتداء ولام التأكيد، فإنها تدخل على الفعل.",
     "en": "By it he guards against the lām of command (lām al-amr), the lām of inception (lām al-ibtidāʾ), and the lām of emphasis (lām al-tawkīd), for these do enter upon the verb."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "المصنف.",
     "en": "[The one who might have “said” is] the author (al-muṣannif)."},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "مكان دخول اللام.",
     "en": "[Had he said this] in place of “the entry of the lām.”"},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: إلا أن المصنف.",
     "en": "That is, [the sense is] “except that the author [did not treat of it].”"},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: لدخول مثل هذا الميم.",
     "en": "That is, [he did not treat] of the inclusion of a mīm such as this [the article-mīm of the Ḥimyarī dialect]."},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: في ضمن اختياره اللام على حرف التعريف، أو في اختياره اللام على الألف واللام، أو الألف — هذه الإشارة.",
     "en": "That is, this indication lies within his choosing “the lām” over “the definite particle,” or in his choosing “the lām” over “the alif and lām,” or over “the alif” — such is the indication."},

    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لأن نقيض التعريف التنكير. ودليله حرف ساكن، فكذا دليل نقيضه، فيتوافق النقيضان في الدال، ويتوافق دليلاهما.",
     "en": "Because the contrary of definiteness is indefiniteness (tankīr); its indicator is a quiescent letter, and likewise the indicator of its contrary, so that the two contraries agree in the indicator, and their two indicators agree."},

    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "مفتوحة مع أنها مكسورة في سائر المواضع؛ لأن الخفة مطلوبة فيها لكثرة استعمالها.",
     "en": "It is given a fatḥa even though [the conjunctive hamza] carries a kasra in all other positions, because lightness (khiffa) is sought in it owing to the frequency of its use."},

    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "وأيضا لو لم يكن كـ«هل» كان المناسب كسرة الهمزة.",
     "en": "Moreover, were it not [analogous] to “hal,” the fitting thing would have been a kasra on the hamza."},

    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: حرف التعريف.",
     "en": "That is, [the pronoun “it” refers to] the definite particle."},

    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "يضعفه شيوع حذفه في الوصل، والعلامة لا تحذف.",
     "en": "This [claim] is weakened by the prevalent elision of it in conjunction (waṣl), whereas a [morphological] marker is not elided."},

    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "أي: حرف التعريف موضوع.",
     "en": "That is, the definite particle is coined [precisely for that purpose]."},

    {"type": "note", "num": "١٣"},
    {"type": "pair",
     "ar": "إن اللام الداخلة على اللفظ الذي أريد به معناه لتعيين المعنى المستقل، ومنحصرة في الجنس والعهد لا اللام مطلقا،",
     "en": "The lām that enters upon a wording by which its own meaning is intended [serves] to specify the independent meaning, and it is confined to [denoting] the genus (jins) and the [external] covenant (ʿahd) — not the lām unrestrictedly;"},
    {"type": "pair",
     "ar": "فإنها قد تدخل على اللفظ، ولا تعيين فيه، فلا عهد ولا جنس كاللام الداخلة على المعرف بالتعريف اللفظي.",
     "en": "for it may enter upon a wording in which there is no specification, so that there is neither covenant nor genus — like the lām entering upon a word made definite by verbal definiteness (al-taʿrīf al-lafẓī)."},
]
