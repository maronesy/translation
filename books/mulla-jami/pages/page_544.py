# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 544 (printed ٥٤٣)."""

PAGE_NUMBER = 544
PRINTED_PAGE = "٥٤٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «ولا يلزم أن يكون السرج حال» at the foot of PDF p. 543 (mid-sentence).
    {"type": "matn",
     "ar": "اشتراء الفرس ملصقا به، فالإلصاق يستلزم المصاحبة[[١]] من غير عكس.",
     "en": "…of buying the horse, attached to it; so adhesion entails accompaniment, but not conversely."},
    {"type": "matn",
     "ar": "٤-(والمقابلة) أي: لإفادة[[٢]] وقوع مجروره في مقابلة شيء آخر، نحو: «بعت هذا بذاك».",
     "en": "4. (And for exchange (muqābala)), that is, for conveying that its governed noun stands in exchange for something else, as in “I sold this for that”."},
    {"type": "matn",
     "ar": "٥-(والتعدية) أي: جعل الفعل اللازم متعديا لتضمنه معنى التصيير، بإدخال الباء على فاعله،",
     "en": "5. (And for transitivization (taʿdiya)), that is, making an intransitive verb transitive, through its including the sense of causing to become (taṣyīr), by attaching the bāʾ to its agent;"},
    {"type": "matn",
     "ar": "فإن معنى «ذهب زيد» صدور الذهاب عنه، ومعنى «ذهبت بزيد» صيرته ذاهبا[[٣]].",
     "en": "for the meaning of “Zayd went” is that going issued from him, while the meaning of “dhahabtu bi-Zaydin” (I took Zayd away) is “I made him go”."},
    {"type": "matn",
     "ar": "والتعدية بهذا المعنى مختصة بالباء[[٤]].",
     "en": "Transitivization in this sense is particular to the bāʾ."},
    {"type": "matn",
     "ar": "وأما التعدية بمعنى إيصال معنى الفعل إلى معموله بواسطة حرف الجر، فالحروف الجارة كلها فيها سواء، لا اختصاص لها بحرف دون حرف.",
     "en": "As for transitivization in the sense of conveying the meaning of the verb to its governed word by means of a preposition, all the prepositions are equal in it; it is not particular to one particle rather than another."},
    {"type": "matn",
     "ar": "٦-(والظرفية) نحو: «جلست بالمسجد» أي: في المسجد.",
     "en": "6. (And for containment), as in “I sat in (bi-) the mosque”, that is, in the mosque."},
    {"type": "matn",
     "ar": "٧-(وزائدة في الخبر في الاستفهام) بـ«هل» لا مطلقا، نحو: «هل زيد بقائم؟» فلا يقال: «أزيد بقائم؟».",
     "en": "7. (And redundant (zāʾida) in the predicate in interrogation) with “hal”, not absolutely, as in “hal Zaydun bi-qāʾimin?” (is Zayd standing?); so one does not say “a-Zaydun bi-qāʾimin?”."},
    {"type": "matn",
     "ar": "(والنفي) بـ«ليس»، نحو: «ليس زيد براكب».",
     "en": "(And in negation) with “laysa”, as in “laysa Zaydun bi-rākibin” (Zayd is not riding),"},
    {"type": "matn",
     "ar": "وبـ«ما» نحو: «ما زيد براكب».",
     "en": "and with “mā”, as in “mā Zaydun bi-rākibin”."},
    {"type": "matn",
     "ar": "فهي تزاد في الخبر في هذه الصور.",
     "en": "So it is added to the predicate in these cases"},
    {"type": "matn",
     "ar": "(قياسا، وفي غيره) أي: غير الخبر الواقع في الاستفهام والنفي (سماعا[[٥]]) سواء",
     "en": "(by analogy; and in other than it), that is, other than the predicate occurring in interrogation and negation, (by hearsay (samāʿan)), whether…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: footnote 1 prints «اشترى الفرس» (verb form) where the sense seems to require «اشتراء الفرس» (the buying of the horse). Transcribed as printed.
    {"type": "pair",
     "ar": "فيه بحث لجواز أن يكون «اشترى الفرس» في مكان يقرب من السرج، ولا يصاحب السرج الفرس في الاشتراء.",
     "en": "This is open to question, since it is possible that “[the buying of] the horse” takes place in a location near the saddle while the saddle does not accompany the horse in the buying."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "خص هذا المعنى بتذكير ما سبق لكونه وسط المعاني المذكورة.",
     "en": "He singled out this meaning for a reminder of what preceded [i.e. the word “li-ifāda”] because it lies in the middle of the meanings mentioned."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سواء ذهب معه، أو لا، فمعنى ذهبت بزيد وأذهبته واحد، كذا قال سيبويه.",
     "en": "Whether he went with him or not; so the meaning of “dhahabtu bi-Zaydin” and “adhhabtuhu” is one. Thus said Sībawayh."},
    {"type": "pair",
     "ar": "وعند المبرد: يجب فيه مصاحبة الفاعل للمفعول به؛ لأن الباء المتعدية عنده بمعنى «مع»",
     "en": "According to al-Mubarrad, the agent’s accompanying the object is necessary in it, because the transitivizing bāʾ according to him is in the sense of “maʿa”."},
    {"type": "pair",
     "ar": "فقوله تعالى: ﴿لذهب بسمعهم﴾ (البقرة:٢٠)، الباء فيه للتأكيد عند المبرد، لا أنه سبحانه ذهب معه، كذا في الرضي.",
     "en": "So in His words, the Exalted, “He would have taken away their hearing” (Qurʾān, Sūrat al-Baqara 2:20), the bāʾ is for emphasis according to al-Mubarrad, not [meaning] that He, Glorified is He, went with it. So it is in al-Raḍī."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وما وقع في عبارة الصرفيين أن تعدية اللازم بحرف الجر في الكل، أي: في الثلاثي المجرد وغيره، فمخصوص بالباء.",
     "en": "What occurs in the wording of the morphologists, that transitivizing the intransitive by a preposition is [possible] in all [verbs], that is, in the bare triliteral and others, is particular to the bāʾ."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "هذا يدل على أن ما يذكره من غير تقييد بالسماع قياسي،",
     "en": "This indicates that what he mentions without restricting it to hearsay is by analogy (qiyāsī);"},
    {"type": "pair",
     "ar": "فاستعمال الباء للاستعانة أو للإلصاق لا يتوقف على السماع، وإلا لقيده به،",
     "en": "so using the bāʾ for seeking aid or for adhesion does not depend on hearsay; otherwise he would have restricted it to that."},
    {"type": "pair",
     "ar": "وقيل: التعدية مقصورة على السماع.",
     "en": "It has been said that transitivization is confined to hearsay."},
]
