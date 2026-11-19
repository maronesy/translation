# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 397 (printed ٣٩٦)."""

PAGE_NUMBER = 397
PRINTED_PAGE = "٣٩٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «النسبة الإضافية،» at the foot of PDF p. 396.
    {"type": "matn",
     "ar": "ومن ظاهر الهيئة التركيبية التي في «تأبط شرا» النسبة التعليقية التي يكون بين الفعل والمفعول،",
     "en": "…and from the outward combinatory form in “Taʾabbaṭa Sharran” the relation of attachment that holds between the verb and its object is understood;"},
    {"type": "matn",
     "ar": "بخلاف مثل: «خمسة عشر»، فإن هيئة تركيب أحد جزئيه مع الآخر لا يدل على النسبة أصلا، كما أن هيئة تركيب أحد شطري «جعفر» مع الآخر لا يدل عليها من غير فرق،",
     "en": "unlike the like of “khamsata ʿashara”, for the form of the combination of one of its parts with the other does not indicate a relation at all, just as the form of the combination of one half of “Jaʿfar” with the other does not indicate one, without any difference."},
    {"type": "matn",
     "ar": "فانطبق الحد على المحدود طردا وعكسا.",
     "en": "So the definition fits the thing defined, both as inclusive and as exclusive (ṭardan wa-ʿaksan)."},
    {"type": "matn",
     "ar": "(فإن تضمن) الجزء (الثاني حرفا) حرف عطف أو غيره[[١]] (بنيا) أي: الجزآن:",
     "en": "(If) the (second) part (contains a particle), a coordinating particle or another, (both are indeclinable), that is, both parts:"},
    {"type": "matn",
     "ar": "الأول: لوقوع آخره في وسط الكلمة الذي ليس محلا للإعراب.",
     "en": "the first, because its end falls in the middle of the word, which is not a place for inflection;"},
    {"type": "matn",
     "ar": "والثاني: لتضمنه الحرف (كـ«خمسة عشر») فإن أصله «خمسة وعشر»، حذفت الواو، وركبت «عشرة» مع «خمسة»",
     "en": "and the second, because it contains the particle, (as “khamsata ʿashara”), for its origin is “khamsatun wa-ʿasharun”: the wāw was dropped and “ʿashara” was combined with “khamsa”;"},
    {"type": "matn",
     "ar": "(و) مثل («حادي عشر» وأخواتها) يعني: أخوات حادي عشر من ثاني عشر إلى تاسع عشر، أو أخوات كل من خمسة عشر وحادي عشر،",
     "en": "(and) like (“ḥādiya ʿashara” and its sisters), meaning the sisters of ḥādiya ʿashara (eleventh) from thāniya ʿashara to tāsiʿa ʿashara, or the sisters of each of khamsata ʿashara and ḥādiya ʿashara."},
    {"type": "matn",
     "ar": "وإنما أورد مثالين[[٢]] ليعلم أن البناء ثابت في هذا المركب[[٣]]، سواء كان أحد جزئيه العدد الزائد على العشرة أو صيغة الفاعل المشتقة منه.",
     "en": "He gave two examples only so that it would be known that indeclinability holds in this compound, whether one of its two parts is the number exceeding ten or the agent-noun form derived from it."},
    {"type": "matn",
     "ar": "وقيل: فيه نظر؛ لأن الثاني فيه لا يتضمن الحرف؛ لأنه لا يراد به «حادي وعشر»؟",
     "en": "It has been said: this is open to question, because the second [example] does not contain the particle, since “ḥādin wa-ʿashrun” is not what is meant by it?"},
    {"type": "matn",
     "ar": "وجوابه[[٤]]: أن المراد بصيغة الفاعل إذا اشتق من أسماء العدد واحد من المشتق منه، لكن لا مطلقا، بل باعتبار وقوعه بعد العدد السابق على المشتق منه،",
     "en": "The answer to it is that what is meant by the agent-noun form, when derived from the number-nouns, is one of that from which it is derived, yet not absolutely, but with respect to its coming after the number preceding that from which it is derived."},
    {"type": "matn",
     "ar": "فإن الثالث مثلا واحد من الثلاثة لكن لا مطلقا، بل باعتبار وقوعه بعد الاثنين،",
     "en": "For “the third”, for example, is one of three, yet not absolutely, but with respect to its coming after two."},
    {"type": "matn",
     "ar": "فلما أخذوا هذه الصيغة من المفردات للدلالة على ما ذكرنا، أرادوا أن يأخذوا مثل ذلك من المركبات، ولا يتيسر ذلك من مجموع الجزأين؛ لأن صيغة فاعل لا تسع حروفهما جميعا[[٥]]،",
     "en": "When they had taken this form from the simple numbers to signify what we mentioned, they wished to take the like of it from the compounds; but that is not feasible from the two parts together, because the form fāʿil cannot hold the letters of both;"},
    {"type": "matn",
     "ar": "فاقتصروا على أخذها من أحد الجزأين؛ إذ في أخذ بعض الحروف من كل جزء مظنة",
     "en": "so they confined themselves to taking it from one of the two parts, since in taking some letters from each part there is a likelihood…"},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 396 (note ١٠) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "وحاصله: أن ظاهر تركيب خمسة عشر تركيب مزجي كبعلبك لا تفهم منه النسبة،",
     "en": "…Its upshot is that the outward combination of khamsata ʿashara is a blended (mazjī) combination, like Baʿlabakk, from which no relation is understood;"},
    {"type": "pair",
     "ar": "لكنه إذا لوحظ أن معناه مجموع العددين يفهم منه أن الواو مقدرة، والأصل خمسة وعشر بخلاف بعلبك.",
     "en": "but when it is observed that its meaning is the sum of the two numbers, it is understood that the wāw is implied and that the origin is khamsatun wa-ʿashrun, unlike Baʿlabakk."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "نحو: بيت بيت أي: لبيت أو إلى بيت.",
     "en": "As “bayta bayta”, that is, “li-bayt” or “ilā bayt” (house to house)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "من نوع واحد من تضمن حرف العطف مع أن الظاهر إيراد المثال الثاني بغير تضمن حرف العطف تعميما للفائدة.",
     "en": "Of a single type, containing a coordinating particle, although the obvious course would have been to give the second example without a contained coordinating particle, to make the benefit general."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: المركب العددي.",
     "en": "That is, the numerical compound."},
    {"type": "pair",
     "ar": "وإنما لم يقل: أورد مثالين أحدهما لتضمن معنى حرف العطف في نفس التركيب، والآخر لتضمنه في أصله؛",
     "en": "He did not say “he gave two examples, one for containing the sense of the coordinating particle in the combination itself, and the other for containing it in its origin”"},
    {"type": "pair",
     "ar": "لأن التعميم في الحكم، أعني: البناء الذي هو المقصود بالذات أولى بالبيان من التعميم في الشرط الذي هو تضمن الحرف.",
     "en": "only because generality in the ruling, namely indeclinability, which is the primary aim, is more deserving of statement than generality in the condition, which is the containing of the particle."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "خلاصته: أن تضمن الحرف أعم من أن يكون بنفسه أو باعتبار مأخذه.",
     "en": "Its gist: containing the particle covers its being so in itself or with respect to its source of derivation."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لزيادتها على ثلاثة.",
     "en": "Because they exceed three."},
]
