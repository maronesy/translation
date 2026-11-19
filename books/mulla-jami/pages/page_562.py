# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 562 (printed ٥٦١)."""

PAGE_NUMBER = 562
PRINTED_PAGE = "٥٦١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فإنهما يجوزان» at the foot of PDF p. 561.
    {"type": "matn",
     "ar": "(في مثل: «إنك وزيد ذاهبان») العطف على محل اسم «إن» بلا مضي الخبر،",
     "en": "…(in the like of “innaka wa-Zaydun dhāhibāni”) coordination with the position of the noun of “inna” without the predicate having passed;"},
    {"type": "matn",
     "ar": "فإنه لما لم يظهر عمل «إن» في اسمه بواسطة بنائه، فكأنها لم تعمل فيه، فلا يلزم المحذور المذكور.",
     "en": "for since the government of “inna” does not show in its noun, because the noun is indeclinable, it is as though it did not govern it, and so the impediment mentioned does not follow."},
    {"type": "matn",
     "ar": "(و«لكن») في جواز العطف[[١]] على محل اسمه (كذلك للاستدراك) أي: مثل «إن»؛ لأنه لا يغير معنى الجملة عما كانت عليه قبل دخوله.",
     "en": "(And “lākinna”, which is for rectification (istidrāk), is likewise) with respect to the permissibility of coordination with the position of its noun, that is, like “inna”, because it does not alter the meaning of the sentence from what it was before it entered."},
    {"type": "matn",
     "ar": "فإن معناه: الاستدراك، وهو لا ينافي المعنى الأصلي[[٢]]، كما أنه لا ينافيه التأكيد،",
     "en": "For its meaning is rectification, and that does not conflict with the original meaning, just as emphasis does not conflict with it."},
    {"type": "matn",
     "ar": "فيجوز اعتبار محل اسمه وعطف شيء عليه بالرفع مثل «إن» المكسورة كما تقول: «لم يخرج زيد ولكن عمرا خارج وبكر»،",
     "en": "So it is permissible to take account of the position of its noun and to coordinate something with it in the nominative, as with “inna” with kasra, as you say: “lam yakhruj Zaydun wa-lākinna ʿAmran khārijun wa-Bakrun (Zayd did not go out, but ʿAmr is going out, and Bakr)”."},
    {"type": "matn",
     "ar": "ولا يجوز في سائر الحروف المشبهة بالفعل[[٣]] العطف على محل اسمها؛ لعدم بقاء المعنى الأصلي فيها، فلا يعتبر محل اسمها.",
     "en": "In the rest of the particles resembling the verb (al-ḥurūf al-mushabbaha bi-l-fiʿl), coordination with the position of their noun is not permitted, because the original meaning does not remain with them, so the position of their noun is not taken into account."},
    {"type": "matn",
     "ar": "(و) أيضا (لذلك) أي: لأجل أن «إن» المكسورة لا تغير معنى الجملة، والمفتوحة تغيره",
     "en": "(And) also (for that reason), that is, because “inna” with kasra does not alter the meaning of the sentence while the fatḥa form alters it,"},
    {"type": "matn",
     "ar": "(دخلت اللام) التي هي لتأكيد معنى الجملة (مع المكسورة) التي هي أيضا لذلك التأكيد (دونها) أي: دون المفتوحة،",
     "en": "(the lām), which is for emphasizing the meaning of the sentence, (enters with the kasra form), which is also for that emphasis, (not with it), that is, not with the fatḥa form,"},
    {"type": "matn",
     "ar": "لكونها بمعنى المفرد، فلا يجتمع معها ما هو لتأكيد معنى الجملة",
     "en": "because the latter has the sense of a single term, so what serves to emphasize the meaning of a sentence does not combine with it."},
    {"type": "matn",
     "ar": "(على الخبر) متعلق بـ«دخلت» أي: دخلت اللام مع المكسورة على الخبر، أي: على خبرها، نحو: «إن زيدا لقائم».",
     "en": "(Upon the predicate) is attached to “entered”; that is, the lām enters with the kasra form upon the predicate, that is, upon its predicate, as in “inna Zaydan la-qāʾimun (Zayd is indeed standing)”;"},
    {"type": "matn",
     "ar": "(أو) دخلت (على الاسم) أي: على اسمها (إذا فصل بينه) أي: بين الاسم (وبينها) أي: بين «إن» نحو: «إن في الدار لزيدا».",
     "en": "(or) it enters (upon the noun), that is, upon its noun, (when there is separation between it), that is, the noun, (and it), that is, “inna”, as in “inna fī l-dāri la-Zaydan (in the house there is indeed Zayd)”;"},
    {"type": "matn",
     "ar": "(أو) دخلت (على ما) وقع (بينهما) أي: بين اسمها وخبرها، نحو: «إن زيدا لطعامك آكل».",
     "en": "(or) it enters (upon what) occurs (between the two), that is, between its noun and its predicate, as in “inna Zaydan la-ṭaʿāmaka ākilun (Zayd is indeed eating your food)”."},
    {"type": "matn",
     "ar": "وإنما خص دخول اللام بهذه الصور؛ لأن فيما عداها يلزم توالي حرفي التأكيد والابتداء أعني: «إن» المكسورة واللام، وهم كرهوا ذلك،",
     "en": "He restricted the entry of the lām to these cases only because in the others there would follow a succession of the two particles of emphasis and inception, namely “inna” with kasra and the lām, which they disliked;"},
    {"type": "matn",
     "ar": "واختاروا تقديم «إن» دون اللام ترجيحا للعامل على ما ليس بعامل.",
     "en": "and they chose to put “inna” first rather than the lām, giving precedence to what governs over what does not govern."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "خلافا لبعضهم.",
     "en": "In disagreement with some of them."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأنه راجع إلى ما قبله لا إلى ما بعده.",
     "en": "Because it refers back to what precedes it, not to what follows it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "خلافا للفراء.",
     "en": "In disagreement with al-Farrāʾ."},
]
