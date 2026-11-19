# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 265 (printed ٢٦٤)."""

PAGE_NUMBER = 265
PRINTED_PAGE = "٢٦٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «لكن المطلق منصرف إلى» from the foot of PDF p. 264.
    {"type": "matn",
     "ar": "الفرد الكامل[[١]]، وهو الوضعي.",
     "en": "…the complete instance, which is the one [settled] by coinage (waḍʿ)."},
    {"type": "matn",
     "ar": "واحترز به عن نحو: «رأيت عينا جارية»، فإن قوله: «جارية» وإن كان يرفع الإبهام عن قوله: «عينا»، لكنه غير مستقر بحسب الوضع[[٢]]، بل نشأ في الاستعمال باعتبار تعدد الموضوع له.",
     "en": "By this he excludes such cases as “I saw a flowing ʿayn (spring)”; for although “flowing” removes the vagueness from “ʿayn,” that vagueness is not settled by coinage; rather it arose in usage from the multiplicity of the meanings for which [the word] was coined."},
    {"type": "matn",
     "ar": "وكذا يقع به الاحتراز عن أوصاف المبهمات[[٣]] نحو: «هذا الرجل»،",
     "en": "Likewise, by it the qualifiers of vague nouns (mubhamāt) are excluded, as in “this man”;"},
    {"type": "matn",
     "ar": "فإن «هذا» مثلا: إما موضوع لمفهوم كلي بشرط استعماله في جزئياته، أو لكل جزئي منه،",
     "en": "for “this,” for example, is coined either for a universal concept on condition that it be used for its particulars, or for each particular of it;"},
    {"type": "matn",
     "ar": "ولا إبهام في هذا المفهوم[[٤]] الكلي، ولا في واحد واحد من جزئياته،",
     "en": "and there is no vagueness in this universal concept, nor in any single one of its particulars;"},
    {"type": "matn",
     "ar": "بل الإبهام إنما نشأ من تعدد الموضوع له أو المستعمل فيه،",
     "en": "rather the vagueness arose only from the multiplicity of what it was coined for or of what it is used for."},
    {"type": "matn",
     "ar": "فتوصيفه بـ«الرجل» يرفع هذا الإبهام، لا الإبهام الواقع في الموضوع له من حيث إنه موضوع له.",
     "en": "So qualifying it by “the man” removes this vagueness, not a vagueness lying in what it was coined for, inasmuch as it was coined for it."},
    {"type": "matn",
     "ar": "وكذا يقع به الاحتراز عن عطف البيان في مثل قولك: «أبو حفص عمر»،",
     "en": "Likewise, by it the explicative apposition (ʿaṭf al-bayān) is excluded, in such an expression as “Abū Ḥafṣ ʿUmar”;"},
    {"type": "matn",
     "ar": "فإن كل واحد من «أبي حفص» و«عمر» موضوع لشخص معين لا إبهام فيه،",
     "en": "for each of “Abū Ḥafṣ” and “ʿUmar” is coined for a determinate individual, with no vagueness in it;"},
    {"type": "matn",
     "ar": "لكن لما كان «عمر» أشهر منه زال بذكره الخفاء الواقع في «أبي حفص» لعدم الاشتهار لا الإبهام الوضعي.",
     "en": "but since “ʿUmar” is better known than it, mentioning it removed the obscurity in “Abū Ḥafṣ” that came from its being less well known, not a vagueness of coinage."},
    {"type": "matn",
     "ar": "(عن ذات) لا عن وصف[[٥]].",
     "en": "(From an entity [dhāt]), not from a quality."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: print reads «من إن لفظ المستقر» (expected «من أن»); transcribed as printed.
    {"type": "pair",
     "ar": "دفع لما ذكره الشيخ الرضي من إن لفظ المستقر لا يدل إلا على الثابت المطلق.",
     "en": "[This is] a rebuttal of what Shaykh al-Raḍī mentioned, namely that the word “mustaqirr” signifies only what is fixed without qualification."},
    {"type": "pair",
     "ar": "ويمكن أن يدفع أيضا بأن الثابت قد يقال في مقابلة المعدوم، وقد يقال في مقابلة الحادث الطارئ، والمراد ههنا هو الثاني.",
     "en": "It can also be rebutted by [noting] that “fixed” (thābit) is sometimes said in contrast to the non-existent, and sometimes in contrast to the newly occurring and supervening; and what is meant here is the second."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ولهذا يكون حقيقة في كل واحد من معانيها، بخلاف العشرين، فإن إطلاقه على خصوص حصة منها مجاز.",
     "en": "For this reason [ʿayn] is literal (ḥaqīqa) in each of its meanings, unlike “twenty,” whose application to a particular portion of them is figurative (majāz)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قيل: يمكن أن يقال: إن التوابع كلها خارجة لذكرها فيما بعد،",
     "en": "It has been said: one could say that the appositives (tawābiʿ) are all excluded because they are treated later."},
    {"type": "pair",
     "ar": "لا يقال: فحينئذ لا حاجة إلى ذكر المستقر؛ لأن صفة المشترك قد خرجت بذلك؛",
     "en": "It should not be objected: “Then there is no need to mention ‘settled,’ since the qualifier of a homonym (mushtarak) has been excluded by that”;"},
    {"type": "pair",
     "ar": "لأنا نقول: يجوز أن يقال: إن ذكر المستقر لإخراج القرائن الأخر المعينة لما يراد من المشترك.",
     "en": "for we say: it may be said that “settled” is mentioned to exclude the other contextual indicators (qarāʾin) that determine what is meant by the homonym."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إن قلت: هذا يقتضي ألا يصح التمييز عن اسم الإشارة",
     "en": "If you say: this entails that a tamyīz from a demonstrative noun is not valid,"},
    {"type": "pair",
     "ar": "مع أن كثيرا منهم ذهبوا إلى أن مثلا في قوله تعالى: ﴿ماذا أراد الله بهذا مثلا﴾ (سورة المدثر:٣١) تمييز عن ذا لا حال عنه.",
     "en": "although many of them held that “mathalan” in His words, the Exalted, “What does Allah intend by this as an example?” (Qurʾān, Sūrat al-Muddaththir 74:31) is a tamyīz from “dhā,” not a ḥāl from it."},
    {"type": "pair",
     "ar": "وكذا الحال في رجلا في «حبذا رجلا».",
     "en": "The same holds for “rajulan” in “ḥabbadhā rajulan” (how excellent a man!)."},
    {"type": "pair",
     "ar": "قلنا: لعل هذا منهم مبني على إرادة مبهم من اسم الإشارة كما في «ربه رجلا ونعم رجلا».",
     "en": "We say: perhaps this view of theirs rests on a vague referent being intended by the demonstrative, as in “rubbahu rajulan” and “niʿma rajulan.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فرق بين النعت والحال والتمييز: بأن وضع الصفة والحال لبيان ثبوت وصف في شيء، فهو يرفع الإبهام عن وصف،",
     "en": "[This] distinguishes between the adjective (naʿt), the ḥāl and the tamyīz: the adjective and the ḥāl are coined to show that a quality belongs to a thing, so they remove vagueness from a quality;"},
    {"type": "pair",
     "ar": "ووضع التمييز لرفع الإبهام عن نفس الاسم وبيان أنه من أي جنس،",
     "en": "whereas the tamyīz is coined to remove vagueness from the noun itself and to show of which genus it is."},
    {"type": "pair",
     "ar": "فرجل عاقل لبيان صفة العقل في «زيد»، و«رطل زيتا» لبيان أن الرطل كائن تحت الزيت.",
     "en": "Thus “an intelligent man” shows the quality of intelligence in “Zayd,” and “a raṭl of oil” shows that the raṭl falls under oil."},
    {"type": "pair",
     "ar": "وذلك فرق واضح لا",
     "en": "This is a clear distinction, not…"},
]
