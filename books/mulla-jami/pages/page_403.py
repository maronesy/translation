# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 403 (printed ٤٠٢)."""

PAGE_NUMBER = 403
PRINTED_PAGE = "٤٠٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «...«كم رجلا ضربته؟»؛ إذا جعلته من قبيل الإضمار على» at the foot of PDF p. 402.
    {"type": "matn",
     "ar": "شريطة التفسير، وقدرت بعده فعلا غير مشتغل عنه، أي: «كم رجلا ضربت ضربته؟»،",
     "en": "…condition of explication (sharīṭat al-tafsīr), and supply after it a verb not diverted from it, that is, “kam rajulan ḍarabta ḍarabtahu?” (how many men did you strike, did you strike him?);"},
    {"type": "matn",
     "ar": "فهو من حيث إن ما بعده فعلا مقدرا غير مشتغل عنه داخل في قاعدة النصب،",
     "en": "for, insofar as what follows it is an implied verb not diverted from it, it falls under the rule of the accusative."},
    {"type": "matn",
     "ar": "وإن لم تجعله من قبيله، ولم تقدر بعده فعلا غير مشتغل، فهو من هذه الحيثية مرفوع داخل في قاعدة الرفع.",
     "en": "If you do not treat it as such and do not supply after it a verb not diverted, then from this respect it is nominative and falls under the rule of the nominative."},
    {"type": "matn",
     "ar": "(وكل ما قبله[[١]]) أي: كل واحد من «كم» الاستفهامية والخبرية وقع قبله (حرف جر) نحو: «بكم درهما اشتريت؟ أو بكم رجل مررت» (أو مضاف) نحو: «غلام كم رجلا ضربت؟ وعبد كم رجل اشتريت» (فمجرور) بحرف الجر أو الإضافة،",
     "en": "(And whatever is preceded by), that is, each instance of interrogative or predicative “kam” before which there occurs (a preposition), as in “bi-kam dirhaman ishtarayta?” (for how many dirhams did you buy?) or “bi-kam rajulin mararta” (by how many a man you passed!), (or an annexed noun (muḍāf)), as in “ghulāma kam rajulan ḍarabta?” (the slave of how many men did you strike?) and “ʿabda kam rajulin ishtarayta” (the slave of how many a man you bought!), (is genitive), by the preposition or by annexation."},
    {"type": "matn",
     "ar": "وإنما جاز تقدم حرف الجر أو المضاف عليهما مع أن لهما صدر الكلام؛ لأن تأخر الجار عن المجرور ممتنع لضعف عمله،",
     "en": "The preposition or annexed noun may precede them, although they have the head of the sentence, only because the genitive-governor coming after what it governs is impossible, owing to the weakness of its government;"},
    {"type": "matn",
     "ar": "فجوز تقديم الجار عليهما على أن يجعل الجار اسما كان أو حرفا مع المجرور ككلمة واحدة مستحقة للصدر.",
     "en": "so placing the genitive-governor before them was allowed, on the basis that the governor, whether a noun or a particle, together with what it governs, is treated as a single word entitled to the head position."},
    {"type": "matn",
     "ar": "(وإلا) أي: وإن لم يكن بعده لا لفظا ولا تقديرا فعل ولا شبه فعل غير مشتغل عنه، ولا قبله حرف جر أو مضاف وكان مجردا عن العوامل اللفظية",
     "en": "(Otherwise), that is, if there is after it, neither expressed nor implied, no verb or quasi-verb not diverted from it, and there is before it no preposition or annexed noun, and it is free of expressed governors,"},
    {"type": "matn",
     "ar": "(فمرفوع) أي: فهو مرفوع (مبتدأ إن لم يكن ظرفا) نحو: «من أبوك؟»[[٢]]",
     "en": "(it is nominative), that is, it is nominative, (a mubtadaʾ if it is not an adverb (ẓarf)), as in “man abūka?” (who is your father?)."},
    {"type": "matn",
     "ar": "وهذا مبني على مذهب سيبويه، فإنه يخبر عنده بمعرفة عن نكرة متضمنة استفهاما.",
     "en": "This rests on the doctrine of Sībawayh, for according to him a definite noun may be the predicate of an indefinite that contains interrogation."},
    {"type": "matn",
     "ar": "وأما عند غير سيبويه، فهذا خبر مقدم على المبتدأ، لكونه نكرة وما بعده معرفة",
     "en": "According to others than Sībawayh, this is a predicate placed before the mubtadaʾ, since it is indefinite and what follows it is definite."},
    {"type": "matn",
     "ar": "(وخبر إن كان ظرفا) نحو: «كم يوما سفرك؟»",
     "en": "(And a khabar if it is an adverb), as in “kam yawman safaruka?” (how many days is your journey?)."},
    {"type": "matn",
     "ar": "فـ«كم» ههنا منصوب المحل أولا[[٣]] داخل تحت قاعدة النصب، باعتبار إعمال الكائن فيه، وداخل في قاعدة الرفع ثانيا لقيامه مقام عامله الذي هو خبر المبتدأ.",
     "en": "Here “kam” is, first, accusative in position, falling under the rule of the accusative with regard to the governing of [the implied] “kāʾin” in it; and, second, it falls under the rule of the nominative because it stands in place of its governor, which is the predicate of the mubtadaʾ."},
    {"type": "matn",
     "ar": "(وكذلك) أي: مثل «كم» في تأتي الوجوه الأربعة الإعرابية بالشرائط المذكورة",
     "en": "(Likewise), that is, like “kam” in admitting the four inflectional possibilities under the stated conditions,"},
    {"type": "matn",
     "ar": "(أسماء الاستفهام والشرط) بمعنى أنه تتأتى تلك الوجوه في جميع هذه الأسماء[[٤]]،",
     "en": "(are the interrogative and conditional nouns), in the sense that those possibilities are available in all of these nouns,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لم يقل: وكل ما له مضاف، أو حرف جر مع أنه أخصر وأوضح لينبه على جواز تقدم المضاف والجار عليها مع اقتضائها صدر الكلام.",
     "en": "He did not say “whatever has an annexed noun or a preposition”, although that is shorter and clearer, in order to point out that the annexed noun and the preposition may precede it although it requires the head of the sentence."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: «نظير الأمثال» printed; «الأمثلة» may be intended. Transcribed as printed.
    {"type": "pair",
     "ar": "نظير الأمثال وينتقض تلك القاعدة بـ«كم رجل صحبك؟»، فإنه يتعين «كم» هناك للخبرية؛",
     "en": "An instance of the examples. That rule is contradicted by “kam rajulin ṣaḥibaka?”, for there “kam” is fixed as predicative,"},
    {"type": "pair",
     "ar": "لأن النكرة لا يكون مبتدأ للمعرفة بالاتفاق فيما عدا مثل: «من أبوك؟ ومررت برجل أفضل منه أبوه»، كما مر.",
     "en": "because by agreement an indefinite is not a mubtadaʾ with a definite [predicate], except in such cases as “man abūka?” and “marartu bi-rajulin afḍalu minhu abūhu” (I passed by a man whose father is better than he), as has preceded."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هكذا ذكره الرضي، وهو غير مرضي؛ لأن المرفوع محلا ليس «كم»، بل الجملة الظرفية، وهي النائبة عن الخبر.",
     "en": "So al-Raḍī mentioned it, and it is not acceptable, because what is nominative in position is not “kam” but the adverbial clause, which is what stands in for the predicate."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إشارة إلى أن الجمع المضاف في قوله: أسماء الاستفهام والشرط الاستغراق بمعنى الكل المجموعي لا كل واحد إلا أنه خص غير «كم» بالقرينة العقلية؛",
     "en": "An indication that the annexed plural in his words “the interrogative and conditional nouns” denotes all-inclusiveness in the sense of the collective whole, not of each one; except that it is restricted to what is other than “kam” by a rational indication,"},
    {"type": "pair",
     "ar": "إذ لا معنى لتشبيه الشيء بنفسه كما في قوله تعالى:",
     "en": "since there is no sense in likening a thing to itself, as in His words, the Exalted:…"},
]
