# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 492 (printed ٤٩١)."""

PAGE_NUMBER = 492
PRINTED_PAGE = "٤٩١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فإن فقد أحد الشرطين، نحو: «أنا إذن أحسن إليك»،» at the foot of PDF p. 491 (mid-sentence).
    {"type": "matn",
     "ar": "وكقولك لمن يحدثك: «إذن أظنك كاذبا» وجب الرفع[[١]].",
     "en": "…and as in your saying to one who speaks to you, “idhan aẓunnuka kādhiban” (then I think you a liar), the nominative is obligatory."},
    # REVIEW: the opening guillemet before «أسلمت» has no printed closing guillemet; transcribed as printed.
    {"type": "matn",
     "ar": "(مثل) قولك لمن قال «أسلمت: (إذن تدخل الجنة) مثل بمثال لا يحتمل إلا الاستقبال.",
     "en": "(As in) your saying to one who said “I have embraced Islam”: (“idhan tadkhula al-jannata” (then you will enter Paradise)). He gave an example that admits only the future."},
    {"type": "matn",
     "ar": "فقوله: «إذن» مبتدأ، وقوله: «إذا لم يعتمد» ظرف للانتصاب الملحوظ معها، كما أشرنا إليه[[٢]].",
     "en": "So his word “idhan” is a subject (mubtadaʾ), and his words “when it does not lean” are an adverbial qualifier of the accusative government understood with it, as we have indicated."},
    {"type": "matn",
     "ar": "وقوله مثل: «إذن تدخل الجنة» خبر المبتدأ، فتمثيل «إذن» بهذا المثال على طريقة تمثيلات أخواتها،",
     "en": "And his words “as in ‘idhan tadkhula al-jannata’” are the predicate of the subject; so exemplifying “idhan” by this example follows the manner of the examples of its sisters;"},
    {"type": "matn",
     "ar": "إلا أنه لما كان انتصاب المضارع بها مشروطا بشرطين أشار إليهما فيما بين المبتدأ والخبر.",
     "en": "except that, since the muḍāriʿ’s being put in the accusative by it is conditional on two conditions, he indicated them between the subject and the predicate."},
    {"type": "matn",
     "ar": "(وإذا وقعت) أي: «إذن» (بعد الواو والفاء فالوجهان) جائزان:",
     "en": "(And when it occurs), that is, “idhan”, (after the wāw and the fāʾ, both treatments) are permissible:"},
    {"type": "matn",
     "ar": "١-«النصب» بناء على ضعف الاعتماد[[٣]] بالعطف؛ لاستقلال المعطوف؛ لأنه جملة.",
     "en": "1. “The accusative”, on the basis of the weakness of the leaning [on what precedes] through coordination, because the coordinated term is independent, being a sentence;"},
    {"type": "matn",
     "ar": "٢-و«الرفع» باعتبار الاعتماد بالعطف وإن ضعف.",
     "en": "2. and “the nominative”, in regard of the leaning through coordination, even if it is weak."},
    {"type": "matn",
     "ar": "(و«كي») التي ينتصب بها المضارع (مثل: «أسلمت كي أدخل الجنة». ومعناها: السببية) أي: سببية ما قبلها لما بعدها، كسببية الإسلام لدخول الجنة في المثال المذكور.",
     "en": "(And “kay”), by which the muḍāriʿ is put in the accusative, (as in “I embraced Islam so that I may enter Paradise”; and its meaning is causation), that is, the causation by what precedes it of what follows it, like the causation of entering Paradise by Islam in the example mentioned."},
    {"type": "matn",
     "ar": "(و«حتى») التي ينتصب بها المضارع بعدها بتقدير «أن» (إذا كان) أي: المضارع (مستقبلا بالنظر إلى ما قبلها)",
     "en": "(And “ḥattā”), after which the muḍāriʿ is put in the accusative by supposing “an”, (when it), that is, the muḍāriʿ, (is future in relation to what precedes it),"},
    {"type": "matn",
     "ar": "وإن كان بالنظر إلى زمان المتكلم[[٤]] ماضيا، أو حالا، أو مستقبلا (بمعنى: «كي») أي: حال كون «حتى»[[٥]] بمعنى «كي» للسببية[[٦]]",
     "en": "even if, in relation to the speaker’s time, it is past, present or future, (in the sense of “kay”), that is, “ḥattā” being in the sense of “kay”, for causation,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "في بعض الصور، فإن المقصود بيان فائدة الاشتراط لا استيفاء إعراب صور الفقدان،",
     "en": "In some cases; for what is intended is to show the benefit of the conditions, not to exhaust the inflection of the cases where they are missing;"},
    {"type": "pair",
     "ar": "فلا يرد أن في صور تقديم الشرط يجب الجزم، فالواجب أن يقول: وجب الرفع والجزم.",
     "en": "so the objection does not hold that in the cases where the condition is placed first the jussive is obligatory, and that he ought therefore to say “the nominative and the jussive are obligatory”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: إلى كونه ظرفا للانتصاب حيث قدر الموصول التي صلتها ينتصب.",
     "en": "That is, to its being an adverbial qualifier of the accusative government, in that he supplied the relative [“which”] whose relative clause is “is put in the accusative”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأن حروف العطف لكونها أصلا في عطف المفردات يقتضي أن يكون المعطوف كالمعمول لما قبله،",
     "en": "Because the coordinating particles, being primarily for coordinating single terms, require that the coordinated term be like what is governed by what precedes it;"},
    {"type": "pair",
     "ar": "لكن بدخوله على الجملة المستقلة ضعف الاعتماد، فكأنه لم يعتمد، فيجوز النصب.",
     "en": "but by its entering upon an independent sentence the leaning is weakened, so it is as though it did not lean, and the accusative is permitted."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: printed «الأولى سواء كان أو ترك المستقبل فتدبر»; the sentence is elliptical as printed. Transcribed as printed; the translation follows the apparent sense.
    {"type": "pair",
     "ar": "الأولى سواء كان أو ترك المستقبل فتدبر.",
     "en": "The better [wording] would be “whether it is…”, or leaving out “future”; so reflect."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إشارة إلى أن قوله: بمعنى كي ظرف مستقر واقع موقع الحال،",
     "en": "An indication that his words “in the sense of kay” are a stable adverbial standing in the position of the circumstantial (ḥāl);"},
    {"type": "pair",
     "ar": "وفائدته الإشارة إلى أنه لا يكون حتى حينئذ بمعناه الحقيقي، أعني: انتهاء الغاية بشرط كون ما بعدها جزء لما قبلها ضعيفا أو قويا في تعلق الفعل السابق.",
     "en": "its benefit is to indicate that “ḥattā” is not then in its proper sense, namely the termination of the extent, on condition that what follows it be a part of what precedes it, weak or strong, in the connection of the preceding verb."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا فائدة لتقييد كي بقوله: للسببية سيما وقد علم معنى كي قبيل ذلك،",
     "en": "There is no benefit in qualifying “kay” by his words “for causation”, especially since the meaning of “kay” was learned shortly before that;"},
    {"type": "pair",
     "ar": "لكن تقييد «إلى» بمعنى انتهاء الغاية للاحتراز عن «إلى» بمعنى «مع».",
     "en": "but qualifying “ilā” by the sense of termination of the extent is to guard against “ilā” in the sense of “maʿa” (with)."},
    {"type": "pair",
     "ar": "فإن قلت: «حتى» أيضا بمعنى انتهاء الغاية فلم قال بمعنى «إلى» ولم يقل: إذا كان بمعناها أو معنى كي؟",
     "en": "If you say: “ḥattā” too means termination of the extent, so why did he say “in the sense of ilā” and not say “when it is in its [own] sense or the sense of kay”?"},
    {"type": "pair",
     "ar": "قلت: كأنه أراد أنه لا يشترط في حتى هذه أن يكون مجروره آخر جزء منه.",
     "en": "I say: it is as though he meant that in this ḥattā it is not a condition that what it governs in the genitive be the last part of it."},
]
